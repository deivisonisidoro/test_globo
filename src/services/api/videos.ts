const apiUrl = process.env.NEXT_PUBLIC_API_URL;


export const addVideo = async (url: string) => {
  
    if (!apiUrl) {
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
  