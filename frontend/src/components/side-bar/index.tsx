'use client';

import Link from 'next/link';
import React, { useState } from 'react';
import { CirclePlusIcon, HomeIcon, MenuIcon } from 'lucide-react';
import { Button } from '@/components/ui/button';

const SideBar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(true);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="flex">
      <aside className={`bg-secondary h-screen ${isOpen ? 'w-64' : 'w-20'} transition-all duration-300 flex flex-col`}>
        
        <div className={`p-4 ${isOpen ? 'justify-start' : 'justify-center'} flex`}>
          <Button
            variant="ghost"
            onClick={toggleSidebar}
          >
            <MenuIcon className="h-6 w-6" />
          </Button>
        </div>

        <nav className="space-y-5">
          <Link href="/" className={`flex ${isOpen ? 'flex-row items-center gap-3 pl-4' : 'flex-col items-center justify-center'} transition-all duration-300`}>
            <HomeIcon className="h-6 w-6" />
            <span className={`text-xs font-medium ${isOpen ? 'text-lg font-semibold' : 'block'}`}>Home</span>
          </Link>

          <Link href="/register" className={`flex ${isOpen ? 'flex-row items-center gap-3 pl-4' : 'flex-col items-center justify-center'} transition-all duration-300`}>
            <CirclePlusIcon className="h-6 w-6" />
            <span className={`text-xs font-medium ${isOpen ? 'text-lg font-semibold' : 'block'}`}>Cadastrar</span>
          </Link>
        </nav>
      </aside>
    </div>
  );
};

export default SideBar;
