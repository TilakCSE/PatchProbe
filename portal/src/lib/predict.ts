import modelJson from "./model.generated.json";
import { predictWithModel, validateModel } from "./portable-inference.mjs";

export type Prediction = { label: string; scores: Record<string, number>; score: number };
const portable = modelJson;
validateModel(portable);
export const modelInfo = portable.model;
export function predict(text: string): Prediction {
  return predictWithModel(portable, text);
}
