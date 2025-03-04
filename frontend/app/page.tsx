import type { User } from "@/store/UserStore";
import { notFound } from "next/navigation";
import MainPage from "./(components)/home";

export default async function Home() {
  try {
    const response = await fetch("http://localhost:8000/users/bob", {
      next: {
        revalidate: 60,
      },
      headers: {
        "Content-Type": "application/json",
      },
    });

    // Log the response status and status text for debugging
    console.log("Response status:", response.status, response.statusText);

    if (response.status === 404) {
      notFound(); // This will trigger the not-found page
    }

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const user = (await response.json()) as User;
    console.log(user);

    if (!user) {
      throw new Error("No user data received");
    }

    return <MainPage user={user} />;
  } catch (error) {
    console.error("Error details:", error);

    // Return a more user-friendly error message
    return (
      <div className="p-8 max-w-md mx-auto">
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <h2 className="text-lg font-semibold text-red-800 mb-2">
            Unable to load user data
          </h2>
          <p className="text-red-600">
            Please check if the API server is running and try again.
          </p>
        </div>
      </div>
    );
  }
}
