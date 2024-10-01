import { z } from "zod";

const videoSchema = z.object({
    url: z.string().url("Por favor, insira uma URL válida"),
  });
  
export {videoSchema}