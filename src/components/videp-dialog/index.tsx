import React, { useEffect } from "react";

interface VideoDialogProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

const VideoDialog: React.FC<VideoDialogProps> = ({ isOpen, onClose, children }) => {
  useEffect(() => {
    const handleEscapeKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose();
      }
    };

    if (isOpen) {
      window.addEventListener('keydown', handleEscapeKey);
    }

    return () => {
      window.removeEventListener('keydown', handleEscapeKey);
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
      <div
        className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center"
        onClick={onClose}
      >
        <div
          className=" bg-zinc-100 dark:bg-gray-800 rounded-lg p-4 max-w-lg w-full"
          onClick={(e) => e.stopPropagation()} // Evita que o clique dentro do modal feche ele
        >
          <button
            className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
            onClick={onClose}
            aria-label="Fechar modal"
          >
            &times;
          </button>
          {children}
        </div>
      </div>
  );
};

export default VideoDialog;
