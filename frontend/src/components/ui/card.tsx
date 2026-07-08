import type { HTMLAttributes, ReactNode } from "react";

type CardProps = HTMLAttributes<HTMLDivElement> & {
  children: ReactNode;
};

export function Card({ children, className = "", ...props }: CardProps) {
  return (
    <section
      className={`rounded-lg border border-slate-200 bg-white shadow-card ${className}`}
      {...props}
    >
      {children}
    </section>
  );
}
