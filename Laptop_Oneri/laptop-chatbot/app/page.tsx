"use client"

import type React from "react"

import { useState, useRef, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Send, Mic, Bot, User, Search, Zap, Briefcase, Wallet, BatteryFull, Rocket, Laptop, Clock, Cpu, DollarSign, Apple } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {
  Sidebar,
  SidebarContent,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton,
  SidebarProvider,
  SidebarTrigger,
  SidebarFooter,
} from "@/components/ui/sidebar"
import { laptopApi, type LaptopRequest, type LaptopResponse } from "@/lib/api"

// Sample data for chat history
const initialConversations = [
  {
    id: 1,
    title: "Oyun Bilgisayarları",
    date: "Bugün",
    messages: [
      {
        id: "welcome",
        content:
          "Merhaba! Ben sizin bilgisayar öneri asistanınızım. Size mükemmel bilgisayarı bulmak için nasıl yardımcı olabilirim?",
        sender: "bot",
        type: "text",
        timestamp: new Date(),
      },
    ] as Message[],
  },
  {
    id: 2,
    title: "Ekonomik Seçenekler",
    date: "Dün",
    messages: [
      {
        id: "welcome",
        content:
          "Merhaba! Ben sizin bilgisayar öneri asistanınızım. Size mükemmel bilgisayarı bulmak için nasıl yardımcı olabilirim?",
        sender: "bot",
        type: "text",
        timestamp: new Date(),
      },
    ] as Message[],
  },
  {
    id: 3,
    title: "MacBook Alternatifleri",
    date: "2 gün önce",
    messages: [
      {
        id: "welcome",
        content:
          "Merhaba! Ben sizin bilgisayar öneri asistanınızım. Size mükemmel bilgisayarı bulmak için nasıl yardımcı olabilirim?",
        sender: "bot",
        type: "text",
        timestamp: new Date(),
      },
    ] as Message[],
  },
  {
    id: 4,
    title: "Öğrenci Bilgisayarları",
    date: "1 hafta önce",
    messages: [
      {
        id: "welcome",
        content:
          "Merhaba! Ben sizin bilgisayar öneri asistanınızım. Size mükemmel bilgisayarı bulmak için nasıl yardımcı olabilirim?",
        sender: "bot",
        type: "text",
        timestamp: new Date(),
      },
    ] as Message[],
  },
]


// Sample laptop data
const sampleLaptops = [
  {
    id: 1,
    name: "TechPro X15",
    image: "/placeholder.svg?height=150&width=200",
    specs: "Intel i7, 16GB RAM, RTX 3070, 1TB SSD",
    price: "18.999 TL",
  },
  {
    id: 2,
    name: "GameMaster Pro",
    image: "/placeholder.svg?height=150&width=200",
    specs: "AMD Ryzen 9, 32GB RAM, RTX 3080, 2TB SSD",
    price: "24.599 TL",
  },
  {
    id: 3,
    name: "UltraBook Air",
    image: "/placeholder.svg?height=150&width=200",
    specs: "Intel i5, 8GB RAM, Entegre Grafik, 512GB SSD",
    price: "12.499 TL",
  },
]

// Message types
type MessageType = "text" | "products"

interface Message {
  id: string
  content: string
  sender: "user" | "bot"
  type: MessageType
  timestamp: Date
  products?: Array<{
    id: string
    name: string
    image: string
    specs: string
    price: string
    url: string
  }>
}

function ProductImage({ productUrl }: { productUrl: string }) {
  const [imgUrl, setImgUrl] = useState<string | null>(null);

  useEffect(() => {
    if (!productUrl) return;
    fetch(`http://localhost:8000/get-image/?url=${encodeURIComponent(productUrl)}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.image_url) setImgUrl(data.image_url);
      });
  }, [productUrl]);

  return (
    <img
      src={imgUrl || "/placeholder.svg"}
      alt="Ürün görseli"
      className="w-full h-48 object-contain"
      style={{ background: "#eee" }}
    />
  );
}


// Sıkça Sorulan Sorular (SSS) kısa ve öz
const faqQuestions = [
  "Oyun için laptop",
  "Ofis için hafif laptop",
  "Uzun pil ömrü",
  "Fiyat/performans",
  "En uygun fiyatlı",
  "Tasarım için laptop",
  "Öğrenci laptopu",
  "En hafif laptop",
  "En güçlü işlemci",
  "Büyük ekran laptop",
  "Asus laptoplar",
  "HP laptoplar",
  "En çok satanlar",
  "En yeni modeller"
];

const quickSuggestionsList = [
  { icon: <span>🎮</span>, text: "Oyun oynamak için güçlü bir laptop istiyorum" },
  { icon: <span>🏢</span>, text: "Ofis için laptop" },
  { icon: <span>💸</span>, text: "Bütçe dostu laptop" },
  { icon: <span>🔋</span>, text: "En iyi pil ömrü" },
  { icon: <span>🚀</span>, text: "Yüksek performanslı laptop" },
  { icon: <span>💎</span>, text: "Premium ultrabook" },
  { icon: <span>⚙️</span>, text: "Intel mi AMD mi?" },
  { icon: <span>💰</span>, text: "15.000 TL altı laptop" },
  { icon: <span>🍏</span>, text: "MacBook Önerileri" },
  { icon: <span>🎓</span>, text: "Öğrenci laptop" },
  { icon: <span>🪶</span>, text: "Hafif laptop" },
  { icon: <span>🎨</span>, text: "Tasarım ve çizim için laptop" },
  { icon: <span>🎬</span>, text: "Video düzenleme için laptop" },
  { icon: <span>🏆</span>, text: "Ofis için hafif ve pil ömrü uzun bir laptop lazım" },
  { icon: <span>🖥️</span>, text: "Büyük ekranlı laptop" },
  { icon: <span>👆</span>, text: "Bu laptop çok pahalı, daha uygun bir şey var mı?" },
]

function FAQPanel({ onSelect }: { onSelect: (q: string) => void }) {
  const [search, setSearch] = useState("");
  const filtered = quickSuggestionsList.filter(s => s.text.toLowerCase().includes(search.toLowerCase()));
  return (
    <aside className="hidden lg:flex flex-col w-80 min-w-[18rem] max-w-[20rem] h-screen bg-slate-900 border-l border-slate-800 p-6">
      <h2 className="text-xl font-bold text-slate-100 mb-4">Hızlı Sorular</h2>
      <div className="relative mb-5">
        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">
          <Search className="w-5 h-5" />
        </span>
        <input
          type="text"
          value={search}
          onChange={e => setSearch(e.target.value)}
          placeholder="Sorularda ara..."
          className="w-full pl-10 pr-3 py-2 rounded-full bg-slate-800 text-slate-100 placeholder-slate-400 border border-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div className="flex flex-col gap-3 overflow-y-auto" style={{ maxHeight: "calc(100vh - 220px)" }}>
        {filtered.map((s, i) => (
          <button
            key={s.text}
            onClick={() => onSelect(s.text)}
            className="flex items-center gap-3 px-4 py-2 rounded-full bg-slate-800 text-slate-100 font-medium hover:bg-slate-700 transition-colors w-full text-left border border-slate-800"
          >
            <span>{s.icon}</span>
            <span>{s.text}</span>
          </button>
        ))}
      </div>
    </aside>
  )
}

export default function Home() {
  const [conversations, setConversations] = useState(initialConversations)
  const [activeConversationId, setActiveConversationId] = useState<number>(conversations[0].id)
  const activeConversation = conversations.find(c => c.id === activeConversationId)
  const [messages, setMessages] = useState<Message[]>(activeConversation?.messages || [])
  const [inputValue, setInputValue] = useState("")
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  // Focus input on load
  useEffect(() => {
    inputRef.current?.focus()
  }, [])

  // Ürünleri metinden ayıklayan fonksiyon
  const parseProductsFromText = (text: string) => {
    // Ürünler ve linkler metin içinde sıralı, ayırıcı olarak 'Urun Linkleri:' kullanılmış
    const [urunlerBolumu, linklerBolumu] = text.split('Urun Linkleri:')
    if (!urunlerBolumu || !linklerBolumu) return []

    // Ürünleri ayıkla
    const urunSatirlari = urunlerBolumu
      .split('\n')
      .filter((line) => line.includes('|'))
      .map((line) => line.trim())
      .filter(Boolean)
      // Başlık satırını çıkar
      .filter((line) => !line.toLowerCase().includes('urun_ad') && !line.toLowerCase().includes('fiyat'))

    // Linkleri ayıkla
    const linkler = linklerBolumu
      .split(/[\s\n]+/)
      .map((l) => l.trim())
      .filter((l) => l.includes('http'))
      .map((l) => {
        let clean = l.replace(/^@+/, '');
        clean = clean.replace(/^https\/\//, 'https://');
        clean = clean.replace(/^http\/\//, 'http://');
        clean = clean.replace(/^https\/([^/])/, 'https://$1');
        clean = clean.replace(/^http\/([^/])/, 'http://$1');
        return clean;
      });

    // Her ürün için kutucuk verisi oluştur
    return urunSatirlari.map((satir, idx) => {
      const [name, price] = satir.split('|').map((s) => s.trim())
      return {
        id: idx.toString(),
        name: name || 'Ürün',
        image: '/placeholder.svg',
        specs: '',
        price: price || '',
        url: linkler[idx] || '#',
      }
    })
  }

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      content: inputValue,
      sender: "user",
      type: "text",
      timestamp: new Date(),
    }

    setMessages((prev) => [...prev, userMessage])
    setConversations((prev) => prev.map(conv =>
      conv.id === activeConversationId
        ? { ...conv, messages: [...conv.messages, userMessage] }
        : conv
    ))
    setInputValue("")
    setIsLoading(true)

    try {
      // API isteği için veriyi hazırla
      const requestData: LaptopRequest = {
        prompt: inputValue
      }

      // API'ye istek at
      const response = await laptopApi.getSuggestions(requestData)

      // Eğer brand_warning varsa, önce onu chat'e ekle
      if (response.brand_warning) {
        const warningMessage: Message = {
          id: (Date.now() + 0.5).toString(),
          content: response.brand_warning,
          sender: "bot",
          type: "text",
          timestamp: new Date(),
        }
        setMessages((prev) => [...prev, warningMessage])
        setConversations((prev) => prev.map(conv =>
          conv.id === activeConversationId
            ? { ...conv, messages: [...conv.messages, warningMessage] }
            : conv
        ))
      }

      // Bot cevabını parse et
      const products = parseProductsFromText(response.cevap)

      let botResponse: Message
      if (products.length > 0) {
        botResponse = {
          id: (Date.now() + 1).toString(),
          content: 'İşte bulduğum ürünler:',
          sender: "bot",
          type: "products",
          timestamp: new Date(),
          products: products,
        }
      } else {
        botResponse = {
          id: (Date.now() + 1).toString(),
          content: response.cevap,
          sender: "bot",
          type: "text",
          timestamp: new Date(),
        }
      }

      setMessages((prev) => [...prev, botResponse])
      setConversations((prev) => prev.map(conv =>
        conv.id === activeConversationId
          ? { ...conv, messages: [...conv.messages, botResponse] }
          : conv
      ))

      // Eğer ask_brand true ise, marka sorma mesajını ekle
      if (response.ask_brand) {
        const brandMessage: Message = {
          id: (Date.now() + 2).toString(),
          content: "🤔 Spesifik bir marka tercihiniz var mı? Örneğin: Asus, Lenovo, HP, Dell, MSI gibi...",
          sender: "bot",
          type: "text",
          timestamp: new Date(),
        }
        setMessages((prev) => [...prev, brandMessage])
        setConversations((prev) => prev.map(conv =>
          conv.id === activeConversationId
            ? { ...conv, messages: [...conv.messages, brandMessage] }
            : conv
        ))
      }
    } catch (error) {
      // Hata durumunda kullanıcıya bilgi ver
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: "Üzgünüm, şu anda yanıt veremiyorum. Lütfen daha sonra tekrar deneyin.",
        sender: "bot",
        type: "text",
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, errorMessage])
      setConversations((prev) => prev.map(conv =>
        conv.id === activeConversationId
          ? { ...conv, messages: [...conv.messages, errorMessage] }
          : conv
      ))
    } finally {
      setIsLoading(false)
    }
  }

  // Yardımcı fonksiyonlar
  const extractBudget = (text: string): number | undefined => {
    const match = text.match(/(\d+)\s*(?:bin|k|tl|lira)/i)
    return match ? parseInt(match[1]) * 1000 : undefined
  }

  const extractUsage = (text: string): string | undefined => {
    const usageTypes = ['oyun', 'iş', 'öğrenci', 'tasarım', 'programlama']
    const lowerText = text.toLowerCase()
    return usageTypes.find(type => lowerText.includes(type))
  }

  const extractPreferences = (text: string): string[] => {
    const preferences = []
    const lowerText = text.toLowerCase()
    
    if (lowerText.includes('hafif')) preferences.push('hafif')
    if (lowerText.includes('pil')) preferences.push('uzun pil ömrü')
    if (lowerText.includes('ekran')) preferences.push('iyi ekran')
    if (lowerText.includes('performans')) preferences.push('yüksek performans')
    
    return preferences
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  const handleQuickSuggestion = (suggestion: string) => {
    setInputValue(suggestion)
    // Focus on input after selecting a suggestion
    inputRef.current?.focus()
  }

  // Linkin başında http/https yoksa ekle, eksik : veya / düzelt
  const ensureHttp = (url: string) => {
    let clean = url.trim().replace(/^@+/, '');
    // Eksik iki nokta varsa düzelt
    clean = clean.replace(/^https\/\//, 'https://');
    clean = clean.replace(/^http\/\//, 'http://');
    clean = clean.replace(/^https\/([^/])/, 'https://$1');
    clean = clean.replace(/^http\/([^/])/, 'http://$1');
    if (clean.startsWith('http://') || clean.startsWith('https://')) return clean;
    return 'https://' + clean.replace(/^\/+/, '');
  }

  // Yeni Konuşma başlat
  const handleNewChat = () => {
    // Eski konuşmayı güncelle (başlık: ilk user mesajı varsa)
    const userFirstMsg = messages.find((msg) => msg.sender === "user")
    const newId = Date.now()
    setConversations((prev) => [
      {
        id: newId,
        title: "Yeni Konuşma",
        date: "Şimdi",
        messages: [
          {
            id: "welcome",
            content:
              "Merhaba! Ben sizin bilgisayar öneri asistanınızım. Size mükemmel bilgisayarı bulmak için nasıl yardımcı olabilirim?",
            sender: "bot" as const,
            type: "text" as const,
            timestamp: new Date(),
          },
        ],
      },
      ...prev.map(conv =>
        conv.id === activeConversationId && userFirstMsg
          ? { ...conv, title: userFirstMsg.content.slice(0, 40) + (userFirstMsg.content.length > 40 ? "..." : ""), date: "Şimdi" }
          : conv
      )
    ])
    setActiveConversationId(newId)
  }

  // Aktif konuşma değişince mesajları güncelle
  useEffect(() => {
    const active = conversations.find(c => c.id === activeConversationId)
    setMessages(active?.messages || [])
  }, [activeConversationId, conversations])

  return (
    <SidebarProvider defaultOpen={true}>
      <div className="flex h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-50">
        {/* Sidebar */}
        <Sidebar className="border-r border-slate-200 dark:border-slate-800">
          <SidebarHeader className="p-4">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-semibold">Bilgisayar Asistanı</h2>
            </div>
          </SidebarHeader>
          <SidebarContent>
            <div className="px-4 py-2">
              <h3 className="text-sm font-medium text-slate-500 dark:text-slate-400">Son Konuşmalar</h3>
            </div>
            <SidebarMenu>
              {conversations.map((chat) => (
                <SidebarMenuItem key={chat.id}>
                  <SidebarMenuButton className="flex justify-between" onClick={() => setActiveConversationId(chat.id)}>
                    <span>{chat.title}</span>
                    <span className="text-xs text-slate-500 dark:text-slate-400">{chat.date}</span>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarContent>
          <SidebarFooter className="p-4">
            <Button variant="outline" className="w-full" onClick={handleNewChat}>
              Yeni Konuşma
            </Button>
          </SidebarFooter>
        </Sidebar>

        {/* Main Chat Area + SSS Panel */}
        <div className="flex flex-1 h-full overflow-hidden">
          {/* Main Chat Area */}
          <div className="flex flex-col flex-1 h-full overflow-hidden">
            {/* Header */}
            <header className="flex items-center justify-between p-4 border-b border-slate-200 dark:border-slate-800">
              <div className="flex items-center">
                <SidebarTrigger className="mr-2" />
                <h1 className="text-xl font-bold">Bilgisayar Önerileri</h1>
              </div>
            </header>

            {/* Chat Messages */}
            <div className="flex-1 overflow-y-auto p-4 space-y-4">
              <AnimatePresence initial={false}>
                {messages.map((message) => (
                  <motion.div
                    key={message.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 0.3 }}
                    className={cn("flex", message.sender === "user" ? "justify-end" : "justify-start")}
                  >
                    <div
                      className={cn(
                        "max-w-[80%] rounded-2xl p-4",
                        message.sender === "user"
                          ? "bg-blue-600 text-white"
                          : "bg-slate-200 dark:bg-slate-800 dark:text-slate-100",
                      )}
                    >
                      <div className="flex items-start gap-2">
                        {message.sender === "bot" && (
                          <div className="flex-shrink-0 mt-1">
                            <div className="bg-blue-500 rounded-full p-1">
                              <Bot size={16} className="text-white" />
                            </div>
                          </div>
                        )}
                        <div className="flex-1">
                          {message.type === "text" && <p>{message.content}</p>}

                          {message.type === "products" && (
                            <div className="space-y-4">
                              <p>{message.content}</p>
                              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-2">
                                {message.products?.map((laptop) => (
                                  <div
                                    key={laptop.id}
                                    className="bg-white dark:bg-slate-900 rounded-lg overflow-hidden shadow-md transition-transform hover:scale-[1.02] min-h-[400px] p-6 flex flex-col justify-between"
                                  >
                                    <ProductImage productUrl={laptop.url} />
                                    <div className="p-4 flex-1 flex flex-col justify-between">
                                      <h3 className="font-bold text-slate-900 dark:text-white text-base md:text-lg">{laptop.name}</h3>
                                      <p className="text-sm text-slate-600 dark:text-slate-300 mt-1">{laptop.specs}</p>
                                      <div className="flex justify-between items-center mt-4">
                                        <span className="font-bold text-blue-600 dark:text-blue-400 text-lg">{laptop.price}</span>
                                        <Button size="sm" variant="outline" asChild>
                                          <a href={ensureHttp(laptop.url)} target="_blank" rel="noopener noreferrer">
                                            Detaylar
                                          </a>
                                        </Button>
                                      </div>
                                    </div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}
                        </div>
                        {message.sender === "user" && (
                          <div className="flex-shrink-0 mt-1">
                            <div className="bg-blue-700 rounded-full p-1">
                              <User size={16} className="text-white" />
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  </motion.div>
                ))}
              </AnimatePresence>
              <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <div className="border-t border-slate-200 dark:border-slate-800 p-4">
              <div className="flex gap-2">
                <Input
                  ref={inputRef}
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  onKeyDown={handleKeyDown}
                  placeholder="Mesajınızı yazın..."
                  disabled={isLoading}
                  className="flex-1"
                />
                <Button onClick={handleSendMessage} disabled={isLoading}>
                  {isLoading ? (
                    <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                  ) : (
                    <Send className="w-5 h-5" />
                  )}
                </Button>
              </div>
              
            </div>
          </div>
          {/* SSS Panel */}
          <FAQPanel onSelect={handleQuickSuggestion} />
        </div>
      </div>
    </SidebarProvider>
  )
}
