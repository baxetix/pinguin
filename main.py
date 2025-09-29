<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Kinder Penguin</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- Header Section -->
  <header class="hero">
    <div class="hero-text">
      <h2>Your Kinder Penguin</h2>
      <h3>Adopt a penguin</h3>
      <p class="breadcrumb">Home / Adopt / Adopt a Penguin</p>
      <p>Adopt a penguin today and support ocean conservation.<br>
      Support our work to study and protect whales and other ocean wildlife by adopting a humpback whale today.</p>
    </div>
    <img src="penguin.png" alt="Penguin" class="hero-img">
  </header>

  <!-- Adoption List -->
  <section class="adoption-list">
    <h2>Penguins Available for Adoption</h2>

    <div class="card">
      <img src="penguin1.png" alt="Penguin Jonny">
      <div class="card-text">
        <p><strong>Nickname:</strong> Jonny</p>
        <p><strong>Patron:</strong> Lily’s Ocean</p>
        <p><strong>ID:</strong> SAYU-1.004</p>
        <p><strong>First sighted:</strong> January 14th, 2012</p>
        <p>SAYU-1.004, known as Jonny, is a humpback penguin with beautiful white flukes...</p>
      </div>
      <button class="adopt-btn" onclick="selectPenguin('Jonny')">Adopt!</button>
    </div>

    <div class="card">
      <img src="penguin2.png" alt="Penguin Bob">
      <div class="card-text">
        <p><strong>Nickname:</strong> Bob</p>
        <p><strong>ID:</strong> CRC-16403</p>
        <p><strong>First sighted:</strong> October 10, 2014</p>
        <p>Bob (CRC-16403) is a well-known whale along the California coast...</p>
      </div>
      <button class="adopt-btn" onclick="selectPenguin('Bob')">Adopt!</button>
    </div>

    <div class="card">
      <img src="penguin3.png" alt="Penguin Ashlynn-Madeleine">
      <div class="card-text">
        <p><strong>Nickname:</strong> Ashlynn-Madeleine</p>
        <p><strong>Patron:</strong> The Craft Market family</p>
        <p><strong>ID:</strong> CRC-10168</p>
        <p><strong>First sighted:</strong> October 26, 1990</p>
        <p>CRC-10168, known as Ashlynn-Madeleine, has been seen multiple times...</p>
      </div>
      <button class="adopt-btn" onclick="selectPenguin('Ashlynn-Madeleine')">Adopt!</button>
    </div>
  </section>

  <!-- Adoption Form -->
  <section class="form-section">
    <h2>Complete Your Adoption</h2>
    <form id="adoptionForm">
      <label>Type of animal you’d like to adopt</label>
      <input type="text" id="animalType" placeholder="Penguin">

      <label>Which penguin would you like to adopt?</label>
      <input type="text" id="penguinChoice" readonly>

      <label>Length of Adoption*</label>
      <select id="adoptionLength">
        <option>One Year</option>
        <option>Two Years</option>
      </select>

      <label>Would you like a printed certificate?</label>
      <select id="certificate">
        <option>Yes, mail a printed certificate</option>
        <option>No, send a digital certificate</option>
      </select>

      <label>Your Name</label>
      <input type="text" id="yourName">

      <label>Your Email Address</label>
      <input type="email" id="yourEmail">

      <label>Cardholder Name</label>
      <input type="text" id="cardName">

      <button type="submit" class="submit-btn">Submit Adoption</button>
    </form>
  </section>

  <script src="script.js"></script>
</body>
</html>
