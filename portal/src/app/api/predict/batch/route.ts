import { NextRequest, NextResponse } from "next/server";
import { ApiInputError, handleError, isRecord, MAX_NOTES, parseBody, validateNote } from "@/lib/api";
import { modelInfo, predict } from "@/lib/predict";

export const runtime = "nodejs";

export async function POST(request: NextRequest) {
  try {
    const body = await parseBody(request);
    if (!isRecord(body) || Object.keys(body).some((key) => key !== "texts") || !Array.isArray(body.texts)) {
      throw new ApiInputError(400, "invalid_batch", "Provide a texts array.");
    }
    if (body.texts.length < 1 || body.texts.length > MAX_NOTES) {
      throw new ApiInputError(400, "invalid_batch", `Batch size must be 1–${MAX_NOTES} notes.`);
    }
    const notes = body.texts.map(validateNote);
    return NextResponse.json({ predictions: notes.map(predict), model: modelInfo }, {
      headers: { "Cache-Control": "no-store" },
    });
  } catch (error) {
    return handleError(error);
  }
}
