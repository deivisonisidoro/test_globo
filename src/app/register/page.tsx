"use client";

import PageContainer from "@/components/page-container";
import { Input } from "@/components/ui/input";
import React from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Button } from "@/components/ui/button";
import { videoSchema } from "./schema";
import { Schema } from "./@types/video-form-data";

const Register: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Schema>({
    resolver: zodResolver(videoSchema),
  });

  const onSubmit = (data: Schema) => {
    console.log(data);
  };

  return (
    <PageContainer>
      <h1 className="text-3xl font-bold mb-6 text-center">Adicionar Vídeo</h1>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="bg-secondary shadow-md rounded-lg p-6 space-y-5 max-w-md mx-auto"
      >
        <div>
          <label htmlFor="url" className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Video URL
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
        <div className="flex justify-end">
          <Button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-md text-base"
          >
            Enviar
          </Button>
        </div>
      </form>
    </PageContainer>
  );
};

export default Register;
