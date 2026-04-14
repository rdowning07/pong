# 🎮 Game Development Curriculum Roadmap

**Goal:** First-principles game development mastery through progressive game building.  
**Language:** Python + Pygame → C++ (later)  
**Timeline:** 14 months  
**Format:** 30 min/day. Write code yourself. Claude checks work and teaches concepts.  

---

## The Ladder

```
Pong → Asteroids → Donkey Kong → Super Mario Bros → Castlevania/Metroid/Zelda → Symphony of the Night → Diablo/WoW
```

Each game is a level. You move on when you can explain every line of your code and the skills for that level are solid.

---

## 🟢 LEVEL 1: Pong
**Status: In Progress**  
**Estimated time: 3-4 weeks**

### What You're Really Learning
Pong is not about Pong. It's about understanding the fundamental architecture that every game uses.

### Skills
- [x] The game loop (input → update → draw)
- [x] Variables and state
- [x] Functions
- [x] Pygame window, clock, fill, flip
- [x] Drawing shapes
- [x] Keyboard input
- [x] Moving objects (position + velocity)
- [x] Collision detection (rectangle vs rectangle, ball vs wall)
- [x] Keeping score
- [x] Game states (playing, game over, restart)

### Architecture Concepts
- What is a frame?
- What is a tick?
- Why does order matter inside the loop?
- What is state and why do we track it?

### Deliverable
A fully playable two-player Pong game. Ball moves, bounces, paddles respond to input, score tracked, game resets on win.

---

## 🟢 LEVEL 2: Asteroids
**Status: Not Started**  
**Estimated time: 4-5 weeks**

### What You're Really Learning
Asteroids introduces motion that isn't just left/right/up/down. Objects rotate. Things spawn and despawn. You start thinking about lists of objects, not just one or two.

### Skills
- [ ] Vectors and 2D math (sin, cos, angles)
- [ ] Rotation
- [ ] Wrap-around screen edges
- [ ] Lists of objects (multiple asteroids, multiple bullets)
- [ ] Clamping and boundary handling
- [ ] Spawning and destroying objects
- [ ] Simple particle effects (debris on explosion)
- [ ] Delta time (frame-rate independent movement)
- [ ] Object-oriented basics — your first classes (Ship, Asteroid, Bullet)

### Architecture Concepts
- What is a vector?
- Why do we use delta time instead of fixed movement?
- What is an object and why do we use classes to represent game entities?
- What does it mean to "update" a list of objects every frame?

### Deliverable
Playable Asteroids. Ship rotates and thrusts, shoots bullets, asteroids split on hit, game ends when ship is hit, score tracked.

---

## 🟢 LEVEL 3: Donkey Kong
**Status: Not Started**  
**Estimated time: 5-6 weeks**

### What You're Really Learning
Donkey Kong introduces gravity, platforms, and enemies with simple AI. This is where games start feeling like games.

### Skills
- [ ] Gravity (velocity that accumulates downward every frame)
- [ ] Jumping (applying upward velocity against gravity)
- [ ] Platform collision (landing on top of things, not just hitting them)
- [ ] Tilemaps (building levels from a grid of tiles)
- [ ] Sprite loading (replacing rectangles with actual images)
- [ ] Simple enemy AI (walk until you hit a wall, turn around)
- [ ] Animation states (idle, walk, jump)
- [ ] Lives system
- [ ] Level loading from data

### Architecture Concepts
- What is gravity in code? (It's just acceleration)
- What is the difference between a hitbox and a sprite?
- What is a tilemap and why do games use them?
- What is an animation state machine?

### Deliverable
A single-screen platformer with a player that runs and jumps, platforms to land on, enemies that patrol, and a goal to reach.

---

## 🟡 LEVEL 4: Super Mario Bros
**Status: Projected**  
**Estimated time: 6-8 weeks**

### What You're Really Learning
Mario is Donkey Kong grown up. Scrolling camera, multiple enemy types, power-ups, multiple levels. This is where you learn to manage complexity.

### Key New Skills
- Scrolling camera (the world is bigger than the screen)
- Multiple enemy types with different behaviors
- Power-up system (state changes on the player)
- Multiple levels with transitions
- Sound effects and music
- More sophisticated collision handling

### Architecture Concepts
- What is a camera and how does it follow a player?
- What is a game object hierarchy?
- How do you manage complexity as a codebase grows?
- Introduction to separating concerns (game logic vs rendering)

---

## 🟡 LEVEL 5: Castlevania / Metroid / Zelda
**Status: Projected**  
**Estimated time: 8-10 weeks**

### What You're Really Learning
Pick one. All three introduce a connected world, persistent player state, and inventory/progression systems. This is where you learn what makes games feel like worlds instead of levels.

### Key New Skills
- Connected rooms / world map
- Persistent state (player health, items, progress saves)
- Inventory system
- More complex enemy AI (patrol, chase, attack patterns)
- Boss fights (multi-phase, telegraphed attacks)
- Basic RPG stats if doing Castlevania/Zelda

### Architecture Concepts
- How do you save and load game state?
- What is a scene/room system?
- What is an inventory and how do you represent it in code?

---

## 🔴 LEVEL 6: Symphony of the Night
**Status: Projected**  
**Estimated time: 10-12 weeks**

### What You're Really Learning
SotN is the graduation project for 2D. It combines everything: exploration, combat, RPG progression, a massive interconnected world, dozens of enemy types, equipment systems. Building even a simplified version requires solid architecture.

### Key New Skills
- Full Metroidvania map system
- Equipment and stat systems
- Spell/ability system
- Enemy variety and AI complexity
- Save system
- Possibly: transition to C++ or a proper engine (Godot, pygame-ce)

### Architecture Concepts
- Entity component systems (ECS) — the architecture used in real game engines
- Data-driven design (defining enemies/items in data files, not code)
- Performance optimization

---

## 🔴 LEVEL 7: Diablo / WoW (3D / Isometric)
**Status: Far Horizon**  
**Estimated time: Open ended**

### What You're Really Learning
This is where 2D mastery transitions to 3D or isometric 3D. New engine (likely Godot or Unity), new language considerations (C#, GDScript, C++), networking if doing WoW-style multiplayer.

### Key New Skills
- 3D space and coordinates
- Isometric rendering (if Diablo-style)
- Networking basics (if multiplayer)
- Procedural generation (dungeon/loot)
- New engine fundamentals

---

## Curriculum Principles

**1. You write every line.**  
No copy-paste from tutorials. Claude checks your work, explains concepts, and points out mistakes. You type the code.

**2. Understand before moving on.**  
You don't advance to the next game until you can explain every line of the current one out loud.

**3. Boring, explicit code first.**  
No clever tricks. No abstractions you don't understand yet. Long, readable, explicit code beats short, clever code you can't explain.

**4. Git every session.**  
Every session ends with a commit. Your history is your learning log.

**5. The README is part of the work.**  
Every project has a README that documents what you built and what you learned. Writing it out cements the knowledge.

---

## Language Path

| Level | Language | Why |
|-------|----------|-----|
| Pong → SotN | Python + Pygame | Fast feedback, you have existing foundation, great for 2D |
| SotN → beyond | Godot (GDScript) or C++ | Real engine, better performance, industry relevant |
| Diablo/WoW | C++ or C# | Performance, engine integration, industry standard |

The language switch happens naturally when Python starts feeling like the ceiling, not before.

---

*Started: April 2026*  
*Target: June 2027*
