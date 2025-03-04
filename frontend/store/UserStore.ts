import { create } from "zustand";

interface User {
  id: number;
  username: string;
  role: "admin" | "user" | "guest";
}

interface UserStore {
  user: User | null;
  setUser: (user: User) => void;
  clearUser: () => void;
}

export const useUserStore = create<UserStore>((set) => ({
  user: null,
  setUser: (user) => {
    localStorage.setItem("user-role", user.role);
    document.cookie = `user-role=${user.role}; path=/`; // Store role in cookie
    set({ user });
  },
  clearUser: () => {
    localStorage.removeItem("user-role");
    document.cookie = `user-role=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`; // Clear cookie
    set({ user: null });
  },
}));
