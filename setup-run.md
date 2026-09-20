# 📚 Full-Stack Book Store Application — User Setup & Run Manual

A comprehensive, step-by-step user manual on how to install dependencies, connect to the database, run the backend APIs, and start the frontend applications for both **Admin** and **Client** portals.

---

## 📌 System Architecture & Ports Overview

| Component | Layer / Framework | Host / Port | Description |
| :--- | :--- | :--- | :--- |
| **Database Server** | MongoDB Community 8.x | `mongodb://localhost:27017` | Database name: `dbProject` |
| **Database GUI** | MongoDB Compass | Desktop GUI | Visual database manager |
| **Admin Backend** | Node.js / Express | `http://localhost:5000` | Admin API for products, users & orders |
| **Client Backend** | Node.js / Express | `http://localhost:4000` | Client API for auth, search & cart |
| **Admin Frontend** | React / Vite | `http://localhost:5173` | Admin dashboard UI |
| **Client Frontend** | React / Vite | `http://localhost:5174` | Customer book shopping store UI |

---

## 🛠️ Prerequisites

Before running the project, make sure you have the following installed on your machine:

1. **Node.js** (v18.x or higher) & **npm**
2. **MongoDB Community Server** (running locally on port `27017`)
3. **MongoDB Compass** (for visual database management)

---

## 🗄️ Step 1: Database Setup (MongoDB & Compass)

### 1.1 Verify MongoDB Server is Running
1. Press `Win + R`, type `services.msc`, and press **Enter**.
2. Scroll to find **`MongoDB Server (MongoDB)`**.
3. Verify that the **Status** is **`Running`**. If not, right-click and choose **`Start`**.

### 1.2 Connect with MongoDB Compass
1. Open **MongoDB Compass**.
2. In the **New Connection** box, enter the connection URI:
   ```text
   mongodb://localhost:27017
   ```
3. Click **Connect** (or **Save & Connect**).
4. You will see the database named **`dbProject`** with the following collections:
   * 📁 `admins` — Admin user credentials
   * 📁 `products` — Book catalogue & images
   * 📁 `registers` — Registered customer accounts
   * 📁 `carts` — User orders and cart items

---

## 📦 Step 2: Install Project Dependencies

Open a terminal at the project root directory (`d:\node2begin\Awd_project`):

### 2.1 Install Admin Dependencies
```bash
cd admin
npm install
cd ..
```

### 2.2 Install Client Dependencies
```bash
cd client
npm install
cd ..
```

---

## 🚀 Step 3: Running the Full Application

To run the entire system, open **4 separate terminal windows** (or split terminals in VS Code / IDE):

### 🖥️ Terminal 1: Admin Backend (Express API)
```bash
cd admin
npx nodemon src/server.cjs
```
> 🟢 Output should display:
> ```text
> Server is running on 5000
> Connected to MongoDB
> ```

---

### 🖥️ Terminal 2: Client Backend (Express API)
```bash
cd client
npx nodemon src/server.cjs
```
> 🟢 Output should display:
> ```text
> Server is running on 4000
> Connected to MongoDB
> ```

---

### 🖥️ Terminal 3: Admin Frontend (React / Vite)
```bash
cd admin
npm run dev
```
> 🟢 Access Admin Portal at: **[http://localhost:5173/](http://localhost:5173/)**

---

### 🖥️ Terminal 4: Client Frontend (React / Vite)
```bash
cd client
npm run dev
```
> 🟢 Access Book Shopping Store at: **[http://localhost:5174/](http://localhost:5174/)**

---

## 📖 Step 4: Application Feature Walkthrough

### 👑 Admin Portal (`http://localhost:5173/`)
1. **Manage Products (`/`)**:
   - Enter **Product Name**, **Image**, **Description**, and **Price**.
   - Click **Add Product** — uploads the image and saves the item to MongoDB.
   - View the live product list in the table below and delete products when needed.
2. **View Orders (`/orders`)**:
   - Displays all customer orders with customer name, date, product image, and price.
3. **Manage Users (`/users`)**:
   - Lists all registered customer accounts with their name, email, gender, city, and profile picture.

---

### 🛒 Customer Store (`http://localhost:5174/`)
1. **Home Page (`/`)**:
   - Browse featured books and learn about the store.
2. **Product Page (`/Product`)**:
   - Search books in real-time with the search bar.
   - View prices and click **Get More Info** to inspect details.
3. **Product Details (`/prodDetail/:id`)**:
   - View book information and click **Add to Cart**.
4. **User Authentication (`/signup` & `/login`)**:
   - Create a new account with a profile picture or sign in with an existing account.
5. **My Orders (`/orders`)**:
   - View all your purchased/ordered items and remove orders.
6. **Contact Us (`/contact`)**:
   - Store global addresses and interactive contact form.

---

## 🔧 Troubleshooting & FAQ

### ❓ Issue: `connect ECONNREFUSED 127.0.0.1:27017`
* **Fix**: MongoDB service is not started. Open `services.msc`, locate `MongoDB Server (MongoDB)`, and click **Start**.

### ❓ Issue: `Port 5000` or `Port 4000` already in use (`EADDRINUSE`)
* **Fix**: Kill the existing process using the port:
  ```powershell
  # Check process using port 5000
  Get-Process -Id (Get-NetTCPConnection -LocalPort 5000).OwningProcess | Stop-Process -Force
  
  # Check process using port 4000
  Get-Process -Id (Get-NetTCPConnection -LocalPort 4000).OwningProcess | Stop-Process -Force
  ```

### ❓ Issue: Images not loading
* **Fix**: Ensure that the `uploads` folders exist:
  - `admin/src/uploads/`
  - `client/src/uploads/`
  Express automatically serves uploaded static images under `/uploads/<filename>`.

---

**Happy Coding & Shopping! 🚀📖**



---

### 👤 Registered Client Account(s)
| Name | Email | Password | City |
| :--- | :--- | :--- | :--- |
| **samarth** | `abc@gmail.com` | `123` | Surat |

> **Login URL:** [http://localhost:5174/login](http://localhost:5174/login)

---

### 🛡️ Admin Account
| Name | Email | Password |
| :--- | :--- | :--- |
| **Admin** | `admin@gamekart.com` | `admin` |

> **Login URL:** [http://localhost:5173/](http://localhost:5173/)