/* eslint-disable @next/next/no-img-element */
"use client";

import React, { useState, useEffect } from "react";
import PageContainer from "@/components/page-container";
import { listVideos } from "@/services/api/videos";
import { Play } from "lucide-react"; // Importe o ícone Play da biblioteca Lucide

interface Video {
  id: string;
  url: string;
}

const Home: React.FC = () => {
  const [videos, setVideos] = useState<Video[]>([]);
  const [currentVideoUrl, setCurrentVideoUrl] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const fetchVideos = async () => {
      setLoading(true);
      setErrorMessage("");

      try {
        const videoList = await listVideos();
        setVideos(videoList.data); // Presume que videoList seja um array de objetos de vídeo
      } catch (error) {
        if (error instanceof Error) {
          setErrorMessage(error.message);
        } else {
          setErrorMessage("An unknown error occurred");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchVideos();
  }, []);

  // Função para extrair o videoId da URL
  const getVideoId = (url: string) => {
    const urlObj = new URL(url);
    return urlObj.searchParams.get("v");
  };

  const handlePlayVideo = (url: string) => {
    setCurrentVideoUrl(url);
  };

  return (
    <PageContainer>
      <h1 className="text-3xl font-bold mb-6 text-center">Lista de Vídeos</h1>

      {loading && <p>Carregando vídeos...</p>}
      {errorMessage && <p className="text-red-500">{errorMessage}</p>}

      {!loading && videos.length === 0 && (
        <p className="text-gray-500 text-center text-xl mt-20">
          Nenhum vídeo disponível no momento. Por favor adicione um novo vídeo.
        </p>
      )}

      {!loading && videos.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {videos.map((video) => {
            const videoId = getVideoId(video.url);
            const thumbnailUrl = `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`;

            return (
              <div
                key={video.id}
                className="flex flex-col items-center bg-zinc-100 dark:bg-gray-800 rounded-lg shadow-md p-4"
              >
                <div className="relative w-full h-[150px] overflow-hidden mb-4">
                  <img
                    src={thumbnailUrl}
                    alt={`Thumbnail for video ${videoId}`}
                    className="absolute top-0 left-0 w-full h-full object-cover cursor-pointer"
                    onClick={() => handlePlayVideo(video.url)}
                  />
                  <button
                    className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-blue-600 hover:bg-blue-700 text-white p-2 rounded-full"
                    onClick={() => handlePlayVideo(video.url)}
                  >
                    <Play className="w-6 h-6" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Reprodutor de vídeo */}
      {currentVideoUrl && (
        <div className="w-full max-w-xl mt-6">
          <h2 className="text-2xl font-semibold mb-4">Reproduzindo Vídeo:</h2>
          <div className="relative pb-[56.25%] h-0 overflow-hidden">
            <iframe
              className="absolute top-0 left-0 w-full h-full"
              src={currentVideoUrl.replace("watch?v=", "embed/")}
              title="YouTube video player"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </div>
        </div>
      )}
    </PageContainer>
  );
};

export default Home;
