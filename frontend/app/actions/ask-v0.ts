"use server";

import { z } from "zod";

const scenarioSchema = z.object({
  scenario: z.string().min(1, "Scenario can't be empty").max(1000, "Scenario is too long"),
  version: z.number().optional().default(2),
});

export async function askV0(formData: FormData) {
  const scenario = formData.get("scenario");
  const version = formData.get("version") ? Number(formData.get("version")) : undefined;

  // Validate the form data using schema
  const validatedFields = scenarioSchema.safeParse({ scenario, version });

  if (!validatedFields.success) {
    return { error: validatedFields.error.flatten().fieldErrors };
  }

  try {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(validatedFields.data),
    });

    if (!response.ok) {
      const errorMessage = `Failed to fetch prediction from API. Status: ${response.status}`;
      return { error: errorMessage };
    }

    const data = await response.json();

    console.log("Prediction Data: ", data);
    if (data && typeof data === "object") {
      console.log("Prediction Data: ", data);
      return { predictions: data };
    }

    return { error: "Unexpected response format from API." };
  } catch (error) {
    console.error("Prediction request error: ", error);
    return { error: "An error occurred while fetching predictions." };
  }
}