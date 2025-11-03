# Guía de Despliegue - QR Farm

## Descripción del Proyecto
QR Farm es una aplicación web para la gestión ganadera que permite escanear códigos QR de animales, gestionar potreros, usuarios y registros de vacunación.

## Arquitectura
- **Frontend**: Vue.js 3 + Vite, desplegado en Vercel
- **Backend**: Flask (Python), desplegado en Render
- **Base de datos**: MySQL alojada en Render

## Despliegue del Frontend (Vercel)

### 1. Preparar el proyecto
```bash
# En la carpeta frontend/
npm install
npm run build
```

### 2. Configurar en Vercel
1. Ve a [vercel.com](https://vercel.com) y crea una cuenta
2. Importa tu repositorio de GitHub/GitLab
3. Configura las variables de entorno:
   - `VITE_API_URL`: URL de tu backend en Render (ej: `https://mi-backend.onrender.com/api`)

### 3. Archivo de configuración
El archivo `vercel.json` ya está configurado para:
- Usar el directorio `dist` como output
- Configurar SPA routing
- Optimizar la build

## Despliegue del Backend (Render)

### 1. Preparar el proyecto
```bash
# En la carpeta backend/
pip install -r requirements.txt
```

### 2. Configurar en Render
1. Ve a [render.com](https://render.com) y crea una cuenta
2. Crea un nuevo servicio web
3. Importa tu repositorio
4. Configura las variables de entorno:

#### Variables de Entorno Requeridas:
```
DB_HOST=tu-host-de-base-datos
DB_USER=tu-usuario-db
DB_PASSWORD=tu-contraseña-db
DB_NAME=nombre-de-tu-base-datos
DB_PORT=3306
SECRET_KEY=tu-clave-secreta-fuerte
JWT_SECRET_KEY=tu-clave-jwt-fuerte
FRONTEND_URL=https://tu-frontend.vercel.app
FLASK_ENV=production
```

### 3. Configuración de Build
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`

## Configuración de Base de Datos

La base de datos MySQL se crea automáticamente en Render junto con el backend usando el archivo `render.yaml`. No necesitas configurar manualmente la base de datos - Render la crea automáticamente cuando despliegues el backend.

Las credenciales de la base de datos se inyectan automáticamente en las variables de entorno del backend:
- `DB_HOST`: Host de la base de datos
- `DB_USER`: Usuario de la base de datos
- `DB_PASSWORD`: Contraseña de la base de datos
- `DB_NAME`: Nombre de la base de datos (qrfarm)
- `DB_PORT`: Puerto de la base de datos

## Verificación del Despliegue

### 1. Verificar Backend
- Health check: `https://tu-backend.onrender.com/api/health`
- Debe retornar: `{"status": "ok", "message": "Servidor activo"}`

### 2. Verificar Frontend
- Abre `https://qr-farm.vercel.app`
- Intenta hacer login con las credenciales por defecto:
  - Email: `admin@qrfarm.com`
  - Password: `admin123`

### 3. Verificar Integración
- El frontend debe poder comunicarse con el backend sin errores CORS
- Las peticiones deben funcionar correctamente

## Solución de Problemas Comunes

### Error CORS
- Verifica que `FRONTEND_URL` en Render coincida exactamente con `https://qr-farm.vercel.app`
- Incluye `https://` en la URL

### Error de Base de Datos
- Verifica las credenciales de conexión
- Asegúrate de que la base de datos esté accesible desde internet
- Revisa los logs de Render para errores específicos

### Error de Build en Vercel
- Verifica que `npm run build` funcione localmente
- Revisa que las variables de entorno estén configuradas correctamente

### Error 500 en Backend
- Revisa los logs de Render
- Verifica que todas las dependencias estén instaladas
- Confirma que las variables de entorno sean correctas

## URLs de Producción
- **Frontend**: `https://qr-farm.vercel.app`
- **Backend**: `https://qr-farm-backend.onrender.com`
- **Base de datos**: MySQL en Render (creada automáticamente)

## Próximos Pasos
1. Subir el proyecto completo a GitHub
2. Conectar el repositorio a Render para el backend
3. Conectar el repositorio a Vercel para el frontend
4. Esperar a que ambos servicios se construyan automáticamente
5. Configurar dominio personalizado si es necesario
6. Configurar monitoreo y logs

## Soporte
Si encuentras problemas durante el despliegue, revisa:
1. Los logs de Vercel y Render
2. Las variables de entorno configuradas
3. La conectividad de la base de datos
4. Los archivos de configuración incluidos en este proyecto