"use server";

import { z } from "zod";

const scenarioSchema = z.object({
  scenario: z.string().min(1, "Scenario can't be empty").max(1000, "Scenario is too long"),
  version: z.number().optional().default(2),
});

export async function get_dependability() {



  try {
    const response = await fetch("http://localhost:8000/get_dependability", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      }
    });

    if (!response.ok) {
      const errorMessage = `Failed to fetch prediction from API. Status: ${response.status}`;
      return { error: errorMessage };
    }

    const data = await response.json();

    console.log("Prediction Data: ", data);
    if (
      data &&
      typeof data === "object" &&
      "system_dependability" in data &&
      "equipment_dependability" in data &&
      Array.isArray(data.equipment_dependability)
    ) {
      return {
        systemDependability: data.system_dependability,
        equipmentDependability: data.equipment_dependability,
      };
    }

    return { error: "Unexpected response format from API." };
  } catch (error) {
    console.error("Prediction request error: ", error);
    return { error: "An error occurred while fetching predictions." };
  }
}