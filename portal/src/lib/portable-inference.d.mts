export type Prediction = { label: string; scores: Record<string, number>; score: number };
export function validateModel(model: unknown): void;
export function predictWithModel(model: unknown, text: string): Prediction;
