import { NextRequest, NextResponse } from "next/server";
import { ApiInputError, handleError, isRecord, parseBody, validateNote } from "@/lib/api";
import { modelInfo, predict } from "@/lib/predict";

export const runtime = "nodejs";

export async function POST(request: NextRequest) {
  try {
    const body = await parseBody(request);
    if (!isRecord(body) || Object.keys(body).some((key) => key !== "text")) {
      throw new ApiInputError(400, "invalid_request", "Provide exactly one text field.");
    }
    const text = validateNote(body.text);
    return NextResponse.json({ prediction: predict(text), model: modelInfo }, {
      headers: { "Cache-Control": "no-store" },
    });
  } catch (error) {
    return handleError(error);
  }
}
