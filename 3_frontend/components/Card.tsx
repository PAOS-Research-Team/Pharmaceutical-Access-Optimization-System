// Reusable card component: displays a title + body in a bordered box.
// Kept dumb/presentational on purpose — no data fetching here, that
// belongs in hooks/ (see hooks/useApiData.ts).

import React from "react";

interface CardProps {
  title: string;
  children: React.ReactNode;
}

export function Card({ title, children }: CardProps) {
  return (
    <div style={{ border: "1px solid #ddd", borderRadius: 8, padding: 16 }}>
      <h3 style={{ margin: "0 0 8px 0" }}>{title}</h3>
      <div>{children}</div>
    </div>
  );
}
