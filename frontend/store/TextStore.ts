// store/TextStore.ts
import { create } from 'zustand';

interface SentenceState {
  sentence: string;
  setSentence: (sentence: string) => void;
  recentChats: string[];
  setRecentChats: (chats: string[]) => void;
}

const useSentenceStore = create<SentenceState>((set) => ({
  sentence: '',
  setSentence: (sentence) => set({ sentence }),
  recentChats: [],
  setRecentChats: (chats) => set({ recentChats: chats }),
}));

export default useSentenceStore;