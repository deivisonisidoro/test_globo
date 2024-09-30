import { Metadata } from 'next';
import { ReactNode } from 'react';


export const metadata: Metadata = {
  title: "Teste Técnico Globo",
  description: "Aplicação para gerenciar URLs de vídeos do YouTube, permitindo a inserção, listagem, reprodução e exclusão dos vídeos.",
};
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
