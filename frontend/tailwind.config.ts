import type { Config } from "tailwindcss";

export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        accent: {
          50: "#ecfdf5",
          100: "#d1fae5",
          600: "#059669",
          700: "#047857"
        }
      },
      boxShadow: {
        card: "0 1px 2px rgba(15, 23, 42, 0.06), 0 12px 32px rgba(15, 23, 42, 0.06)"
      }
    }
  },
  plugins: []
} satisfies Config;
