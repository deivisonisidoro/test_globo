import { z } from "zod";
import { videoSchema } from "../schema";

export type Schema = z.infer<typeof videoSchema>