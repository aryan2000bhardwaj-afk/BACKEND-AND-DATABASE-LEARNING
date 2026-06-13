import { pipeline } from "@xenova/transformers";

let extractor = null;

async function getExtractor() {
    if (!extractor) {
        extractor = await pipeline(
            "feature-extraction",
            "Xenova/all-MiniLM-L6-v2"
        );
    }
    return extractor;
}

export async function generateVector(text) {
    const model = await getExtractor();

    const feature = await model(text, {
        pooling: "mean",
        normalize: true
    });

    return Array.from(feature.data);
}

export function cosineSimilarity(Q, T) {
    if (!Q || !T) return 0;
    if (Q.length !== T.length) return 0;

    let dot = 0;
    let mag1 = 0;
    let mag2 = 0;

    for (let i = 0; i < Q.length; i++) {
        dot += Q[i] * T[i];
        mag1 += Q[i] * Q[i];
        mag2 += T[i] * T[i];
    }

    mag1 = Math.sqrt(mag1);
    mag2 = Math.sqrt(mag2);

    if (mag1 === 0 || mag2 === 0) {
        return 0;
    }

    return dot / (mag1 * mag2);
}