export interface LaptopRequest {
  budget?: number;
  usage?: string;
  preferences?: string[];
  prompt: string;
}

export interface LaptopResponse {
  recommendations: Array<{
    model: string;
    price: number;
    specs: {
      processor: string;
      ram: string;
      storage: string;
      display: string;
    };
    score: number;
  }>;
  cevap: string;
  brand_warning?: string;
  ask_brand?: boolean;
}

const API_URL = 'http://localhost:8000';

export const laptopApi = {
  async getRecommendations(data: LaptopRequest): Promise<LaptopResponse> {
    const response = await fetch('/api/laptop', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('API isteği başarısız oldu');
    }

    return response.json();
  },

  async getAllLaptops(): Promise<LaptopResponse> {
    const response = await fetch('/api/laptop', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('API isteği başarısız oldu');
    }

    return response.json();
  },

  async getSuggestions(request: LaptopRequest): Promise<LaptopResponse> {
    try {
      const response = await fetch(`${API_URL}/get-suggestions/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        throw new Error('API isteği başarısız oldu');
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('API hatası:', error);
      throw error;
    }
  },
}; 