import SideBar from "@/components/side-bar";
import { ModeToggle } from "@/components/mode-toggle"; // Importing the ModeToggle
import { ReactNode } from "react";

interface PageContainerProps {
  children: ReactNode;
}

export default function PageContainer({ children }: PageContainerProps) {
  return (
    <div className="flex flex-col min-h-screen">
      <div className="flex flex-1">
        <SideBar />
        <main className="flex-1 p-6">
          <div className="flex justify-end mb-6">
            <ModeToggle />
          </div>
          {children}
        </main>
      </div>
    </div>
  );
}
