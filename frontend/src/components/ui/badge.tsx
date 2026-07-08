type BadgeProps = {
  found: boolean;
};

export function StatusBadge({ found }: BadgeProps) {
  return (
    <span
      className={`inline-flex items-center rounded-full px-2.5 py-1 text-xs font-medium ${
        found
          ? "bg-accent-100 text-accent-700"
          : "bg-red-50 text-red-700"
      }`}
    >
      {found ? "Found" : "Not Found"}
    </span>
  );
}
