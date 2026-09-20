# 🎨 GameKart CSS Design System & Multi-Language AI Prompt Guide

A comprehensive, standalone CSS documentation and implementation manual for **GameKart E-Commerce Platform** (Customer Storefront + Admin Control Center). This document contains the full CSS design tokens, universal component classes, and ready-to-use **AI Prompts** to port or implement this exact same UI across **PHP (Core PHP / Laravel / CodeIgniter)**, **Python (Django / Flask)**, **ASP.NET Core**, **React / Next.js**, or **Pure HTML5**.

---

## 📑 Table of Contents
1. [🎨 Design Tokens & CSS Variables (`:root`)](#1--design-tokens--css-variables-root)
2. [🔤 Google Fonts & Typography CDN](#2--google-fonts--typography-cdn)
3. [📦 Complete Standalone CSS Stylesheet](#3--complete-standalone-css-stylesheet)
   - Global Resets & Body
   - Client Navigation Bar (`.main-nav`)
   - Hero Banner & Call-to-Action
   - Product Catalog Grid & Item Cards (`.product-card`)
   - Search Bar & Filter Controls
   - Product Details & Specifications View
   - Authentication Cards (`.auth-card` - Login / Signup)
   - Shopping Cart & Order Tracking Tables
   - Admin Layout & Sticky Sidebar (`.wrapper`, `.sidebar`)
   - Admin Inventory Tables & Form Controls
   - Responsive Media Queries
4. [🤖 Master AI Prompts to Generate Pages in PHP / Other Languages](#4--master-ai-prompts-to-generate-pages-in-php--other-languages)
   - [Prompt 1: Core PHP + MySQL Full-Stack Conversion](#prompt-1-core-php--mysql-full-stack-conversion)
   - [Prompt 2: Laravel (Blade Engine) Conversion](#prompt-2-laravel-blade-engine-conversion)
   - [Prompt 3: Python Django / Flask (Jinja2) Conversion](#prompt-3-python-django--flask-jinja2-conversion)
   - [Prompt 4: ASP.NET Core Razor Pages Conversion](#prompt-4-aspnet-core-razor-pages-conversion)
5. [📄 Ready-to-Use PHP Component Templates](#5--ready-to-use-php-component-templates)
   - `header.php`
   - `footer.php`
   - `product-card.php`
   - `admin-table.php`

---

## 1. 🎨 Design Tokens & CSS Variables (`:root`)

Include these CSS custom properties at the top of your global stylesheet. They define the signature **GameKart Clean Purple/Violet Theme**:

```css
:root {
  /* ==========================================================================
     GameKart Design System - Clean Premium Purple/Violet Theme
     ========================================================================== */
  
  /* Primary & Accent Palette */
  --theme-primary: #CE5CFF;           /* Vivid Gaming Neon Purple */
  --theme-primary-dark: #B838EE;      /* Deep Purple Hover State */
  --theme-primary-rgb: 206, 92, 255;
  --theme-secondary: #CE5CFF;
  --theme-accent: #CE5CFF;
  --theme-light-pink: #F6EBFF;        /* Soft Lavender Background Tint */
  
  /* Background & Surface Palette */
  --theme-bg: #FFFFFF;                /* Crisp White Main Canvas */
  --theme-bg-start: #FFFFFF;
  --theme-surface: #FCF8FF;           /* Ultra-Light Lavender Card Surface */
  --theme-surface-soft: #F6EBFF;      /* Soft Highlight Surface */
  --theme-surface-elevated: #FCF8FF;
  
  /* Text & Ink Palette */
  --theme-ink: #17121A;               /* Dark Charcoal (Headings & Strong text) */
  --theme-text: #665A68;              /* Slate Purple-Gray (Body text) */
  --theme-muted: #8E7F91;             /* Muted Gray for Subtitles/Meta */
  --theme-white: #FFFFFF;
  
  /* Borders & Dividers */
  --theme-border: #E5C7F7;            /* Soft Violet Border */
  --theme-border-accent: #CE5CFF;     /* Highlighted Violet Border */
  
  /* Status Colors */
  --theme-danger: #DC2626;            /* Red for delete/errors */
  --theme-danger-bg: rgba(220, 38, 38, 0.08);
  --theme-success: #16A34A;           /* Green for in-stock/success */
  --theme-warning: #D97706;           /* Amber for pending status */
  
  /* Navigation, Sidebar & Tables */
  --theme-sidebar: #FCF8FF;
  --theme-sidebar-dark: #FFFFFF;
  --theme-sidebar-text: #17121A;
  --theme-sidebar-muted: #665A68;
  --theme-table-header: #F6EBFF;
  --theme-footer: #FCF8FF;
  --theme-footer-text: #665A68;
  
  /* Typography Families */
  --font-display: "Rajdhani", "Space Grotesk", sans-serif;
  --font-logo: "Orbitron", sans-serif;
  --font-body: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  
  /* Flat Minimal Shadows */
  --theme-shadow-soft: none;
  --theme-shadow-card: none;
  --theme-shadow-hover: none;
}
```

---

## 2. 🔤 Google Fonts & Typography CDN

Paste this `<link>` tag into the `<head>` of your PHP/HTML files:

```html
<!-- Google Fonts: Orbitron (Logos), Rajdhani (Headings), Plus Jakarta Sans (Body) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
```

---

## 3. 📦 Complete Standalone CSS Stylesheet

Save this entire block as `gamekart.css` or `style.css`:

```css
/* ==========================================================================
   GAMEKART UNIFIED STYLESHEET (Client + Admin)
   ========================================================================== */

* {
  box-sizing: border-box;
}

html {
  color-scheme: light;
}

body {
  margin: 0;
  padding: 0;
  font-family: var(--font-body);
  background: var(--theme-bg);
  color: var(--theme-ink);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

/* Custom Minimal Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: #FFFFFF;
}
::-webkit-scrollbar-thumb {
  background: var(--theme-border);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #D5A6EE;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  color: var(--theme-primary);
  text-decoration: none;
  transition: color 0.15s ease;
}
a:hover {
  color: var(--theme-primary-dark);
}

/* Headings Typography */
h1, h2, h3, h4, h5, h6,
.section-title, .brand-title, .card-title {
  font-family: var(--font-display);
  font-weight: 700;
  letter-spacing: 0.5px;
  color: var(--theme-ink);
  margin-top: 0;
}

/* ==========================================================================
   BUTTONS & BADGES
   ========================================================================== */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: var(--theme-primary);
  color: #FFFFFF !important;
  border: 1px solid var(--theme-primary);
  padding: 10px 22px;
  font-family: var(--font-display);
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  border-radius: 6px;
  cursor: pointer;
  text-decoration: none;
}
.btn-primary:hover {
  background: var(--theme-primary-dark);
  border-color: var(--theme-primary-dark);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: var(--theme-surface-soft);
  color: var(--theme-ink) !important;
  border: 1px solid var(--theme-border);
  padding: 10px 20px;
  font-family: var(--font-display);
  font-size: 14px;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
}
.btn-secondary:hover {
  background: #E5C7F7;
}

.btn-danger {
  background: var(--theme-danger);
  color: #FFFFFF !important;
  border: 1px solid var(--theme-danger);
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
}
.btn-danger:hover {
  background: #B91C1C;
}

.badge {
  display: inline-block;
  padding: 4px 10px;
  font-size: 12px;
  font-weight: 700;
  border-radius: 20px;
  text-transform: uppercase;
}
.badge-purple {
  background: var(--theme-surface-soft);
  color: var(--theme-primary-dark);
  border: 1px solid var(--theme-border);
}
.badge-success {
  background: #DCFCE7;
  color: #15803D;
}
.badge-danger {
  background: #FEE2E2;
  color: #B91C1C;
}

/* ==========================================================================
   CLIENT NAVIGATION BAR
   ========================================================================== */
.client-navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: var(--theme-surface);
  border-bottom: 1px solid var(--theme-border);
  padding: 14px 28px;
}
.navbar-container {
  max-width: 1240px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.navbar-logo {
  font-family: var(--font-logo);
  font-size: 22px;
  font-weight: 900;
  letter-spacing: 1.5px;
  color: var(--theme-ink);
  display: flex;
  align-items: center;
  gap: 8px;
}
.navbar-logo span {
  color: var(--theme-primary);
}
.navbar-links {
  display: flex;
  align-items: center;
  gap: 24px;
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav-item a {
  font-family: var(--font-display);
  font-size: 16px;
  font-weight: 600;
  color: var(--theme-ink);
  letter-spacing: 0.4px;
}
.nav-item a:hover,
.nav-item.active a {
  color: var(--theme-primary);
}
.nav-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

/* ==========================================================================
   HERO BANNER SECTION
   ========================================================================== */
.hero-section {
  background: linear-gradient(135deg, #FCF8FF 0%, #F6EBFF 100%);
  border-bottom: 1px solid var(--theme-border);
  padding: 64px 20px;
  text-align: center;
}
.hero-content {
  max-width: 800px;
  margin: 0 auto;
}
.hero-tag {
  display: inline-block;
  background: #FFFFFF;
  border: 1px solid var(--theme-border);
  color: var(--theme-primary-dark);
  font-family: var(--font-display);
  font-weight: 700;
  padding: 6px 16px;
  border-radius: 30px;
  font-size: 13px;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 16px;
}
.hero-title {
  font-size: 44px;
  line-height: 1.15;
  color: var(--theme-ink);
  margin-bottom: 14px;
}
.hero-subtitle {
  font-size: 17px;
  color: var(--theme-text);
  margin-bottom: 28px;
}

/* ==========================================================================
   SEARCH BAR & FILTERS
   ========================================================================== */
.search-container {
  max-width: 680px;
  margin: 0 auto 36px;
  position: relative;
}
.search-input {
  width: 100%;
  padding: 14px 20px 14px 46px;
  font-size: 15px;
  font-family: var(--font-body);
  border: 1.5px solid var(--theme-border);
  border-radius: 8px;
  background: #FFFFFF;
  color: var(--theme-ink);
  outline: none;
}
.search-input:focus {
  border-color: var(--theme-primary);
}
.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--theme-muted);
}

/* ==========================================================================
   PRODUCT CATALOG GRID & CARDS
   ========================================================================== */
.products-wrapper {
  max-width: 1240px;
  margin: 40px auto;
  padding: 0 20px;
}
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 28px;
}
.product-card {
  background: var(--theme-surface);
  border: 1px solid var(--theme-border);
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 100%;
}
.product-card:hover {
  border-color: var(--theme-primary);
}
.product-thumb {
  height: 220px;
  background: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  border-bottom: 1px solid var(--theme-border);
}
.product-thumb img {
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
}
.product-body {
  padding: 18px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.product-title {
  font-size: 18px;
  margin-bottom: 8px;
  color: var(--theme-ink);
}
.product-desc {
  font-size: 13.5px;
  color: var(--theme-text);
  margin-bottom: 16px;
  flex-grow: 1;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.product-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 14px;
  border-top: 1px dashed var(--theme-border);
}
.product-price {
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 700;
  color: var(--theme-primary-dark);
}

/* ==========================================================================
   AUTHENTICATION FORM CARDS (Login & Register)
   ========================================================================== */
.auth-wrapper {
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background: #FFFFFF;
}
.auth-card {
  width: 100%;
  max-width: 440px;
  background: var(--theme-surface);
  border: 1px solid var(--theme-border);
  border-radius: 12px;
  padding: 32px;
}
.auth-header {
  text-align: center;
  margin-bottom: 24px;
}
.auth-title {
  font-size: 28px;
  color: var(--theme-ink);
  margin-bottom: 6px;
}
.form-group {
  margin-bottom: 18px;
}
.form-label {
  display: block;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--theme-ink);
  margin-bottom: 6px;
}
.form-control {
  width: 100%;
  padding: 11px 14px;
  border: 1px solid var(--theme-border);
  border-radius: 6px;
  background: #FFFFFF;
  color: var(--theme-ink);
  font-size: 14px;
  outline: none;
}
.form-control:focus {
  border-color: var(--theme-primary);
}

/* ==========================================================================
   TABLES & ORDER VIEWS
   ========================================================================== */
.table-container {
  width: 100%;
  overflow-x: auto;
  border: 1px solid var(--theme-border);
  border-radius: 8px;
  background: #FFFFFF;
}
.gamekart-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}
.gamekart-table th {
  background: var(--theme-table-header);
  color: var(--theme-ink);
  font-family: var(--font-display);
  font-size: 14px;
  font-weight: 700;
  padding: 14px 16px;
  border-bottom: 1px solid var(--theme-border);
}
.gamekart-table td {
  padding: 14px 16px;
  border-bottom: 1px solid var(--theme-border);
  font-size: 14px;
  color: var(--theme-text);
  vertical-align: middle;
}
.gamekart-table tr:nth-child(even) {
  background: #FCF8FF;
}
.table-thumb {
  width: 50px;
  height: 50px;
  border-radius: 6px;
  object-fit: contain;
  background: #FFFFFF;
  border: 1px solid var(--theme-border);
  padding: 2px;
}

/* ==========================================================================
   ADMIN DASHBOARD & SIDEBAR LAYOUT
   ========================================================================== */
.admin-layout {
  display: flex;
  min-height: 100vh;
  background: #FFFFFF;
}
.admin-sidebar {
  width: 260px;
  background: var(--theme-surface);
  border-right: 1px solid var(--theme-border);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  position: sticky;
  top: 0;
  height: 100vh;
}
.admin-brand {
  padding: 22px 20px;
  border-bottom: 1px solid var(--theme-border);
  font-family: var(--font-logo);
  font-size: 18px;
  font-weight: 800;
  color: var(--theme-ink);
}
.admin-brand span {
  color: var(--theme-primary);
}
.admin-nav {
  list-style: none;
  padding: 16px 12px;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.admin-nav-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 6px;
  font-family: var(--font-display);
  font-size: 15px;
  font-weight: 600;
  color: var(--theme-text);
}
.admin-nav-link:hover,
.admin-nav-link.active {
  background: var(--theme-surface-soft);
  color: var(--theme-primary-dark);
  font-weight: 700;
}
.admin-main {
  flex-grow: 1;
  padding: 32px;
  background: #FFFFFF;
  overflow-y: auto;
}
.admin-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--theme-border);
}

/* ==========================================================================
   FOOTER
   ========================================================================== */
.client-footer {
  background: var(--theme-footer);
  border-top: 1px solid var(--theme-border);
  padding: 40px 20px;
  text-align: center;
  color: var(--theme-footer-text);
  font-size: 14px;
  margin-top: 60px;
}

/* ==========================================================================
   RESPONSIVE DESIGN (MEDIA QUERIES)
   ========================================================================== */
@media (max-width: 992px) {
  .admin-layout {
    flex-direction: column;
  }
  .admin-sidebar {
    width: 100%;
    height: auto;
    position: relative;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 32px;
  }
  .navbar-container {
    flex-direction: column;
    gap: 14px;
  }
  .products-grid {
    grid-template-columns: 1fr;
  }
  .admin-main {
    padding: 18px;
  }
}
```

---

## 4. 🤖 Master AI Prompts to Generate Pages in PHP / Other Languages

Copy and paste any of the following prompts into an AI assistant (or use directly in your IDE) to generate complete code in different languages using this exact same styling.

---

### Prompt 1: Core PHP + MySQL Full-Stack Conversion
```text
You are a senior PHP and Web Developer.
I want you to build a complete E-Commerce project in Core PHP (Procedural or OOP) and MySQL named "GameKart".

STYLING & CSS REQUIREMENTS:
- Use the exact CSS classes and color tokens from the GameKart Design System.
- Primary Theme: Purple/Violet (#CE5CFF, #B838EE), Background: Crisp White (#FFFFFF), Surface: #FCF8FF, Borders: #E5C7F7, Headings: Dark Charcoal (#17121A).
- Fonts: "Orbitron" for logo, "Rajdhani" for headings, "Plus Jakarta Sans" for body.
- Reusable classes: .btn-primary, .product-card, .gamekart-table, .client-navbar, .auth-card, .admin-sidebar.

PAGES TO CREATE IN PHP:
1. config/db.php -> PDO or mysqli database connection to MySQL (db_gamekart).
2. includes/header.php & includes/footer.php -> Modular navigation and footer.
3. index.php -> Homepage with Hero banner and featured gaming products.
4. products.php -> Catalog with search filtering (GET query) and product cards.
5. product-detail.php?id=X -> Specifications and Add to Cart button.
6. cart.php -> Cart items table with total calculation and "Order Now" button.
7. login.php & signup.php -> User authentication with session management and avatar file upload.
8. admin/products.php -> Admin product management table with Add Product form (multipart image upload to /uploads/).
9. admin/orders.php -> Admin orders review table with user and product JOIN queries.
10. admin/users.php -> Registered customers table.

Ensure all HTML uses the GameKart CSS classes so the website renders identically to the React version.
```

---

### Prompt 2: Laravel (Blade Engine) Conversion
```text
You are an expert Laravel Developer.
Please convert the GameKart React project into a Laravel 11 application using Blade templates and MySQL.

REQUIREMENTS:
- Store the GameKart CSS in public/css/gamekart.css.
- Use Blade layouts: resources/views/layouts/app.blade.php (Customer) and resources/views/layouts/admin.blade.php (Admin).
- Reusable Blade components: <x-product-card :product="$product" />, <x-admin-table />.
- Implement Controllers: ProductController, CartController, AuthController, AdminProductController, AdminOrderController.
- Handle multipart file uploads to storage/app/public/products using Intervention Image or standard Laravel store().
- Use the GameKart CSS classes (.product-card, .client-navbar, .gamekart-table, .auth-card, etc.).
```

---

### Prompt 3: Python Django / Flask (Jinja2) Conversion
```text
You are a full-stack Python Web Developer.
Build the GameKart E-Commerce Store using Python Django (or Flask) with SQLite/PostgreSQL.

REQUIREMENTS:
- Place the GameKart CSS in static/css/gamekart.css.
- Use base.html and admin_base.html templates with Jinja2 / Django template tags ({% block content %}).
- Implement Models: Product (pname, price, description, pimg), UserRegister, CartOrder.
- Create views and URL routes matching: / (Home), /products (Catalog & Search), /cart, /signup, /login, /admin/products, /admin/orders.
- Apply the GameKart styling classes throughout all templates.
```

---

### Prompt 4: ASP.NET Core Razor Pages Conversion
```text
You are an ASP.NET Core developer.
Create an ASP.NET Core MVC / Razor Pages application for GameKart E-Commerce.

REQUIREMENTS:
- Put the GameKart CSS in wwwroot/css/gamekart.css.
- Configure _Layout.cshtml with the GameKart navigation and Orbitron/Rajdhani Google fonts.
- Use ViewModels and Entity Framework Core for Product, User, and Cart entities.
- Render product grids and tables using the GameKart CSS class system.
```

---

## 5. 📄 Ready-to-Use PHP Component Templates

Here are direct, copy-paste PHP files for your project:

### File: `includes/header.php`
```php
<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo isset($page_title) ? $page_title . ' - GameKart' : 'GameKart — Gaming Gear & Accessories Store'; ?></title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
    
    <!-- GameKart CSS -->
    <link rel="stylesheet" href="css/gamekart.css">
</head>
<body>

<nav class="client-navbar">
    <div class="navbar-container">
        <a href="index.php" class="navbar-logo">
            GAME<span>KART</span>
        </a>
        <ul class="navbar-links">
            <li class="nav-item"><a href="index.php">Home</a></li>
            <li class="nav-item"><a href="products.php">Products</a></li>
            <li class="nav-item"><a href="orders.php">My Orders</a></li>
            <li class="nav-item"><a href="contact.php">Contact</a></li>
        </ul>
        <div class="nav-actions">
            <?php if (isset($_SESSION['user_id'])): ?>
                <span class="badge badge-purple">Hi, <?php echo htmlspecialchars($_SESSION['user_name']); ?></span>
                <a href="logout.php" class="btn-secondary" style="padding: 6px 12px; font-size: 13px;">Logout</a>
            <?php else: ?>
                <a href="login.php" class="btn-secondary" style="padding: 6px 14px;">Login</a>
                <a href="signup.php" class="btn-primary" style="padding: 6px 16px;">Sign Up</a>
            <?php endif; ?>
        </div>
    </div>
</nav>
```

---

### File: `includes/footer.php`
```php
<footer class="client-footer">
    <div class="navbar-container">
        <p style="margin: 0 0 8px; font-weight: 600;">© <?php echo date('Y'); ?> GameKart E-Commerce Platform. All Rights Reserved.</p>
        <p style="margin: 0; color: var(--theme-muted); font-size: 13px;">Built for TYBCA Minor Project (AWD & WFS) — Full-Stack Gaming Accessories Store</p>
    </div>
</footer>

</body>
</html>
```

---

### File: `product-card.php` (Reusable PHP Product Snippet)
```php
<?php
// Expects $product array with keys: id, pname, price, description, pimg
?>
<div class="product-card">
    <div class="product-thumb">
        <img src="uploads/<?php echo htmlspecialchars($product['pimg']); ?>" alt="<?php echo htmlspecialchars($product['pname']); ?>">
    </div>
    <div class="product-body">
        <h3 class="product-title"><?php echo htmlspecialchars($product['pname']); ?></h3>
        <p class="product-desc"><?php echo htmlspecialchars($product['description']); ?></p>
        <div class="product-footer">
            <div class="product-price">₹<?php echo number_format($product['price']); ?></div>
            <a href="product-detail.php?id=<?php echo $product['id']; ?>" class="btn-primary" style="padding: 6px 14px; font-size: 13px;">
                Info & Cart
            </a>
        </div>
    </div>
</div>
```

---

### File: `admin-table.php` (Reusable Admin Table Snippet)
```php
<div class="table-container">
    <table class="gamekart-table">
        <thead>
            <tr>
                <th>Photo</th>
                <th>Product Name</th>
                <th>Price (INR)</th>
                <th>Description</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($products_list as $item): ?>
            <tr>
                <td>
                    <img src="../uploads/<?php echo htmlspecialchars($item['pimg']); ?>" class="table-thumb" alt="Product">
                </td>
                <td style="font-weight: 600; color: var(--theme-ink);">
                    <?php echo htmlspecialchars($item['pname']); ?>
                </td>
                <td style="font-family: var(--font-display); font-weight: 700; color: var(--theme-primary-dark); font-size: 16px;">
                    ₹<?php echo number_format($item['price']); ?>
                </td>
                <td style="max-width: 260px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    <?php echo htmlspecialchars($item['description']); ?>
                </td>
                <td>
                    <a href="delete-product.php?id=<?php echo $item['id']; ?>" class="btn-danger" onclick="return confirm('Are you sure you want to delete this product?');">
                        Delete
                    </a>
                </td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</div>
```

---

## 🎯 Summary

With this markdown guide, you have:
1. **The complete GameKart CSS design system** extracted from both client and admin portals.
2. **Ready-to-use AI prompts** to convert the project into **PHP, Laravel, Python, or ASP.NET**.
3. **Copy-paste PHP templates** for headers, footers, product cards, and admin tables.
