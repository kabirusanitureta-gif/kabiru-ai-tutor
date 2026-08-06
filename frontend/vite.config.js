import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Kabiru AI Tutor - Vite config
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 5173,
  },
  preview: {
    host: true,
    port: 5173,
  },
})
