import { NextRequest, NextResponse } from "next/server";

export const MAX_NOTES = 100;
export const MAX_CHARS = 10_000;
const MAX_BODY_BYTES = 1_100_000;

export function apiError(status: number, code: string, message: string) {
  return NextResponse.json({ error: { code, message } }, { status });
}

export async function parseBody(request: NextRequest): Promise<unknown> {
  if (!request.headers.get("content-type")?.toLowerCase().includes("application/json")) {
    throw new ApiInputError(415, "unsupported_media_type", "Send a JSON request body.");
  }
  const statedLength = Number(request.headers.get("content-length") ?? 0);
  if (statedLength > MAX_BODY_BYTES) {
    throw new ApiInputError(413, "body_too_large", "Request body is too large.");
  }
  const raw = await request.text();
  if (new TextEncoder().encode(raw).length > MAX_BODY_BYTES) {
    throw new ApiInputError(413, "body_too_large", "Request body is too large.");
  }
  try {
    return JSON.parse(raw);
  } catch {
    throw new ApiInputError(400, "invalid_json", "Request body must contain valid JSON.");
  }
}

export class ApiInputError extends Error {
  constructor(public status: number, public code: string, message: string) {
    super(message);
  }
}

export function validateNote(value: unknown): string {
  if (typeof value !== "string") {
    throw new ApiInputError(400, "invalid_note", "Each release note must be a string.");
  }
  const clean = value.replace(/\s+/gu, " ").trim();
  if (!clean || Array.from(clean).length > MAX_CHARS) {
    throw new ApiInputError(400, "invalid_note", `Each note must contain 1–${MAX_CHARS} characters.`);
  }
  return clean;
}

export function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

export function handleError(error: unknown) {
  if (error instanceof ApiInputError) return apiError(error.status, error.code, error.message);
  return apiError(500, "prediction_failed", "Prediction is unavailable. Please try again later.");
}
