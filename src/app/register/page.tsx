"use client";

import PageContainer from "@/components/page-container";
import { Input } from "@/components/ui/input";
import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Button } from "@/components/ui/button";
import { videoSchema } from "./schema";

import { addVideo } from "@/services/api/videos"; // Importa a função da API
import { z } from "zod";


export type Schema = z.infer<typeof videoSchema>

const Register: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Schema>({
    resolver: zodResolver(videoSchema),
  });

  const onSubmit = async (data: Schema) => {
    setLoading(true);
    setErrorMessage("");
    setSuccessMessage("");

    try {
      const response = await addVideo(data.url);
      
      setSuccessMessage(response.message);
    } catch (error) {
      if (error instanceof Error) {
        console.error("Error adding video:", error.message);
        setErrorMessage(error.message);
      } else {
        console.error("An unknown error occurred");
        setErrorMessage("Ocorreu um erro desconhecido");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <PageContainer>
      <h1 className="text-3xl font-bold mb-6 text-center">Adicionar Novo Vídeo</h1>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="bg-zinc-100 dark:bg-gray-800 shadow-md rounded-lg p-6 space-y-5 max-w-md mx-auto"
      >
        <div>
          <label htmlFor="url" className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            URL do Vídeo
          </label>
          <Input
            id="url"
            type="url"
            placeholder="https://www.youtube.com/watch?v=example"
            {...register("url")}
            className={`mt-1 border rounded-md p-2 transition duration-150 ease-in-out 
              focus:border-blue-500 focus:ring focus:ring-blue-200 
              dark:bg-gray-700 dark:border-gray-600 
              ${errors.url ? "border-red-500" : "border-gray-300"}`}
          />
          {errors.url && (
            <p className="mt-1 text-red-500 text-sm">{errors.url.message}</p>
          )}
        </div>

        {errorMessage && <p className="text-red-500">{errorMessage}</p>}
        {successMessage && <p className="text-green-500">{successMessage}</p>}

        <div className="flex justify-end">
          <Button type="submit" className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-md text-base" disabled={loading}>
            {loading ? "Adicionando..." : "Adicionar Vídeo"}
          </Button>
        </div>
      </form>
    </PageContainer>
  );
};

export default Register;
