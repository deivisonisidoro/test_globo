import React from 'react';

interface SnackbarProps {
  message: string;
  onClose: () => void;
}

const Snackbar: React.FC<SnackbarProps> = ({ message, onClose }) => {
  return (
    <div className="fixed bottom-5 left-5 z-50"> {/* Alterado para 'left-5' */}
      <div className="bg-red-600 text-white p-4 rounded-md shadow-md">
        {message}
        <button className="ml-4" onClick={onClose}>
          &times;
        </button>
      </div>
    </div>
  );
};

export default Snackbar;
