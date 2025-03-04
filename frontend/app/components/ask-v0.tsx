"use client";

import { useState } from "react";
import { useFormStatus } from "react-dom";
import { askV0 } from "../actions/ask-v0";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import {
  Loader2,
  Send,
  Image,
  FileCode,
  Upload,
  Layout,
  UserPlus,
} from "lucide-react";

type PredictionCategory = Record<string, number>;
type Prediction = Record<string, PredictionCategory>;

export function AskV0() {
  const [predictions, setPredictions] = useState<any | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);

    try {
      const result = await askV0(formData);
      if (result && "predictions" in result) {
        setPredictions(result.predictions);
        setError(null);
      } else if (result && "error" in result) {
        console.error(result.error);
        setError(result.error);
        setPredictions(null);
      }
    } catch (err) {
      console.error(err);
      setError("An unexpected error occurred.");
      setPredictions(null);
    }
  }

  const renderCategoryOutput = (
    category: string,
    values: PredictionCategory
  ) => {
    return (
      <div key={category} className="mb-4 bg-black/10 rounded-lg p-4">
        <h4 className="text-md font-semibold capitalize text-zinc-200">
          {category}:
        </h4>
        <ul className="space-y-1">
          {Object.entries(values).map(([key, value], index) => (
            <li key={index} className="flex justify-between text-zinc-300">
              <span className="capitalize">{key}:</span>
              <span>{(value * 100).toFixed(2)}%</span>
            </li>
          ))}
        </ul>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <div className="max-w-3xl mx-auto space-y-8">
        <h1 className="text-4xl font-bold text-center mb-2">
          What can I help you ship?
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <Textarea
            name="scenario"
            placeholder="Ask v0 a question..."
            className="min-h-[100px] w-full bg-zinc-900 border-zinc-800 text-white placeholder:text-zinc-400 rounded-xl transition-all duration-200 focus:min-h-[200px]"
          />

          <div className="flex flex-wrap gap-2">
            <Button
              variant="outline"
              type="button"
              className="bg-zinc-900 text-zinc-300 border-zinc-800 hover:bg-zinc-800"
            >
              <Image className="w-4 h-4 mr-2" />
              Clone a Screenshot
            </Button>
            <Button
              variant="outline"
              type="button"
              className="bg-zinc-900 text-zinc-300 border-zinc-800 hover:bg-zinc-800"
            >
              <FileCode className="w-4 h-4 mr-2" />
              Import from Figma
            </Button>
            <Button
              variant="outline"
              type="button"
              className="bg-zinc-900 text-zinc-300 border-zinc-800 hover:bg-zinc-800"
            >
              <Upload className="w-4 h-4 mr-2" />
              Upload a Project
            </Button>
            <Button
              variant="outline"
              type="button"
              className="bg-zinc-900 text-zinc-300 border-zinc-800 hover:bg-zinc-800"
            >
              <Layout className="w-4 h-4 mr-2" />
              Landing Page
            </Button>
            <Button
              variant="outline"
              type="button"
              className="bg-zinc-900 text-zinc-300 border-zinc-800 hover:bg-zinc-800"
            >
              <UserPlus className="w-4 h-4 mr-2" />
              Sign Up Form
            </Button>
          </div>

          <div className="flex justify-end">
            <SubmitButton />
          </div>
        </form>

        {error && <p className="text-red-400 text-sm">{error}</p>}

        {predictions && (
          <div className="space-y-6 bg-zinc-900/50 rounded-xl p-6">
            <h3 className="text-xl font-semibold text-zinc-100">
              Predictions:
            </h3>

            <div className="space-y-6">
              {/* Predclass Output */}
              <div>
                <h4 className="text-lg font-medium text-zinc-200 mb-3">
                  Predclass Output:
                </h4>
                {predictions.predclass_output &&
                  Object.entries(predictions.predclass_output).map(
                    ([category, values], index) =>
                      renderCategoryOutput(category, values)
                  )}
              </div>

              {/* LFapplier Output */}
              <div>
                <h4 className="text-lg font-medium text-zinc-200 mb-3">
                  LFapplier Output:
                </h4>
                {predictions.LFapplier_output &&
                  Object.entries(predictions.LFapplier_output).map(
                    ([category, values], index) =>
                      renderCategoryOutput(category, values)
                  )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function SubmitButton() {
  const { pending } = useFormStatus();

  return (
    <Button
      type="submit"
      disabled={pending}
      className="bg-zinc-800 hover:bg-zinc-700 text-white"
    >
      {pending ? (
        <>
          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
          Predicting...
        </>
      ) : (
        <>
          <Send className="mr-2 h-4 w-4" />
          Get Predictions
        </>
      )}
    </Button>
  );
}
