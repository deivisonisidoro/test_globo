import { ReactNode } from 'react';

interface RegisterLayoutProps {
    children: ReactNode
}

export default function RegisterLayout  ({ children }: RegisterLayoutProps){
  return (
    <>
        {children}
    </>
  );
}
