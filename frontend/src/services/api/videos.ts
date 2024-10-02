
const apiUrl = process.env.NEXT_PUBLIC_API_URL;
console.log(apiUrl);


export const addVideo = async (url: string) => {
  console.log(apiUrl);

  if (!apiUrl) {
    console.error("API URL:", apiUrl);
    throw new Error("API URL is not defined");
  }

  try {
    const response = await fetch(`${apiUrl}/videos`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    return data;
  } catch (error) {
    console.error("Error adding video:", error);
    throw error;
  }
};

export const listVideos = async () => {
  console.log(apiUrl);

  if (!apiUrl) {
    throw new Error("API URL is not defined");
  }

  try {
    const response = await fetch(`${apiUrl}/videos`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail);
    }

    return data; // Presume que a resposta seja uma lista de vídeos
  } catch (error) {
    console.error("Error fetching videos:", error);
    throw error;
  }
};

// Função para deletar um vídeo
export const deleteVideo = async (videoId: string) => {
  if (!apiUrl) {
    throw new Error("API URL is not defined");
  }

  try {
    const response = await fetch(`${apiUrl}/videos/${videoId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail);
    }
  } catch (error) {
    console.error("Error deleting video:", error);
    throw error;
  }
};
