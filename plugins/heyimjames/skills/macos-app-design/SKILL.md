---
name: macos-app-design
description: "Design and build OpenAI-Codex-quality native macOS apps with the polish of Linear, Things 3, Granola, Notion Calendar, Arc Browser, Raycast, and Apple's own apps. Use this skill whenever the user is building, reviewing, or polishing a native Swift/SwiftUI Mac app — including AI coding tools, productivity apps, note-taking apps, design tools, dev tools, menu-bar utilities, or document-based apps. Targets macOS 14 (Sonoma) minimum and especially macOS 26 (Tahoe / Liquid Glass). Triggers on: macOS, Mac app, native Mac, SwiftUI Mac, AppKit, NSWindow, NSWindowController, NSToolbar, NSStatusItem, NSMenuItem, NavigationSplitView, sidebar, toolbar, menu bar, MenuBarExtra, status bar item, traffic lights, window restoration, multi-window, document-based app, NSDocument, .commands, .menu, .keyboardShortcut, focus state, .onHover, hover state, cursor, .contextMenu, right-click, three-column layout, Mac sidebar, Inspector pattern, Liquid Glass macOS, Tahoe, command palette, Cmd-K, Cmd-N, Cmd-S, Cmd-shift-Z, Dock badge, NSApplication, Sparkle, App Store distribution, notarization, Developer ID, code editor, syntax highlighting, SF Mono, monospaced, terminal integration, Stage Manager, Mission Control, Continuity, Spotlight integration, CoreSpotlight, Quick Look, Universal Control, Apple Intelligence, Codex, Granola, Linear Mac, Raycast, Cursor, Things 3, Arc Browser, native Mac feel."
metadata:
  short-description: Design native macOS apps with the polish of OpenAI Codex, Linear, Things 3, Granola, and Raycast.
---

# macOS App Design — Design Engineering Skill

A taste guide for building macOS apps that feel like they were built by people who use Macs all day. Every value below is opinionated and specific — drawn from studying OpenAI's Codex app (the modern reference for AI-powered Mac apps), Linear's Mac client, Things 3, Granola, Raycast, Notion Calendar, Arc Browser, and Apple's own first-party apps.

This skill assumes a native Swift/SwiftUI Mac app, targeting macOS 14 (Sonoma) minimum and ideally macOS 26 (Tahoe — Liquid Glass). It pairs with the iOS skills in this marketplace — many polish principles transfer, but **Mac is its own platform with its own conventions**, and ignoring them is the single most common way Mac apps feel "off."

---

## Output format — required

When this skill is invoked to review macOS code or recommend changes, **always output recommendations as a markdown table** with three columns:

| Before | After | What this changes |
| --- | --- | --- |
| The current code, value, or approach (quote the user's actual code when possible) | The recommended replacement — **specific**, with exact values | One sentence on what the user will *see, feel, or experience* differently |

Three rules:
1. **Before** quotes the user's actual code where possible.
2. **After** is specific. Exact NSWindow sizes, exact keyboard shortcuts, exact toolbar item placements.
3. **What this changes** is *experiential or visual*, not abstract.

Output ONE table with multiple rows for multi-recommendation reviews. Use `—` for Before if the user hasn't implemented that thing yet.

**Examples drawn from this skill:**

| Before | After | What this changes |
| --- | --- | --- |
| Single-window app with everything in one view | `NavigationSplitView { sidebar } content: { content } detail: { detail }` with `.navigationSplitViewColumnWidth(min: 200, ideal: 220)` | Three-column layout reads as a proper Mac app instead of a stretched iOS app — Mac users have decades of muscle memory for the sidebar pattern |
| Button with `.onTapGesture` only | `Button(action: ...) { ... }.keyboardShortcut("n", modifiers: .command)` | Action gains Cmd-N keyboard binding — Mac users expect every meaningful action to have a shortcut |
| `Color.gray` for sidebar background | `.background(.regularMaterial)` (or `.background(.bar)` on macOS 26) | Sidebar picks up Liquid Glass translucency — content underneath shows through subtly, matches Finder/Mail/Notes |

This format is required for every recommendation output by this skill.

---

## Philosophy

> An iOS app on a Mac feels embarrassed. A web app in an Electron shell feels apologetic. A real Mac app feels at home.

The Codex Mac app is the right modern reference because it answers a question every AI tool builder is asking: "what does an AI coding tool *look like* as a native Mac citizen?" The answer it gives:

- **Sidebar**: conversations + projects, behaves exactly like Mail's mailbox list. Drag to reorder. Right-click for context menu. Type-to-select.
- **Toolbar**: minimal, unified with title bar, only the actions you actually need (new, search, share, settings).
- **Command palette**: `Cmd-K` opens an in-app palette — same gesture as Raycast, Linear, Things 3.
- **Code rendering**: SF Mono in code blocks, syntax-highlighted, with hover-to-copy.
- **Multi-window**: open a project in its own window. Each window has independent state.
- **Menu bar**: full menu hierarchy. Every action is in a menu. Every menu item has a shortcut.
- **Keyboard-first**: you can use the entire app without touching the trackpad.

That's the bar.

### Three pillars

**1. Mac convention over invention.** Mac users have 20+ years of muscle memory for sidebars, toolbars, menu bars, keyboard shortcuts, and traffic lights. Violating these conventions to be "different" is the #1 way Mac apps lose trust. If you're not sure how a control should behave, look at Mail, Notes, Finder, or System Settings first.

**2. Keyboard-first, mouse-enhanced.** Mac is fundamentally a keyboard machine. The trackpad is enhancement, not core. Every meaningful action gets a keyboard shortcut. Every list supports type-to-select. Every interactive element supports `Tab` focus. The trackpad adds hover states, scroll, swipe gestures — but never *replaces* the keyboard.

**3. Density without clutter.** Mac screens are big — 13-inch up to 32-inch displays. You can show more information than on iOS without the screen feeling busy, but only if you respect spatial hierarchy. Linear's Mac client shows ~3× more information per screen than its iOS app and feels *less* busy because the layout respects Mac conventions (sidebars, columns, fixed regions).

The pixel-pushers' rules:
- **The menu bar is sacred.** A Mac app without a meaningful menu bar feels broken. Even a single-purpose utility should have File / Edit / View / Window / Help.
- **The traffic lights are part of your design.** Don't hide them. Don't move them more than necessary. Don't replace them.
- **The keyboard shortcut hint is part of the UI.** Mac users *look at* `⌘ N` in menus and tooltips to learn the app.
- **Hover is information.** Every clickable element should have a hover state. Mac users move the mouse to discover.
- **Window restoration is not optional.** When the user reopens the app, every window should be exactly where they left it, with exactly the content they had.

---

## Section index

| Section | Topic |
| --- | --- |
| [§1](#1-window-architecture) | Window architecture — sizes, traffic lights, title bars, restoration |
| [§2](#2-the-sidebar-pattern) | The sidebar pattern — NavigationSplitView, three columns |
| [§3](#3-toolbars) | Toolbars — unified style, item placement, principal actions |
| [§4](#4-the-menu-bar) | The menu bar — required menus, item conventions, custom additions |
| [§5](#5-keyboard-shortcuts--focus) | Keyboard shortcuts & focus — every action has one |
| [§6](#6-the-command-palette-cmd-k) | The command palette (Cmd-K) — Raycast/Linear/Codex pattern |
| [§7](#7-mouse--trackpad--hover-states) | Mouse, trackpad & hover states |
| [§8](#8-context-menus-right-click) | Context menus (right-click) |
| [§9](#9-multi-window--document-architecture) | Multi-window & document architecture |
| [§10](#10-status-bar--menubarextra-utilities) | Status bar & MenuBarExtra utilities |
| [§11](#11-liquid-glass-on-macos-tahoe--macos-26) | Liquid Glass on macOS (Tahoe / macOS 26) |
| [§12](#12-typography-on-mac) | Typography on Mac |
| [§13](#13-color--material) | Color & material — semantic, OKLCH, materials |
| [§14](#14-spacing--density) | Spacing & density |
| [§15](#15-drag-and-drop) | Drag and drop |
| [§16](#16-code-app-specifics-syntax-highlighting-monospace-terminals) | Code-app specifics — syntax, monospace, terminals, file trees |
| [§17](#17-settings-window) | Settings window |
| [§18](#18-about-help--app-shortcuts) | About, Help, & App Shortcuts |
| [§19](#19-spotlight-quick-look--continuity) | Spotlight, Quick Look & Continuity |
| [§20](#20-stage-manager-spaces--mission-control) | Stage Manager, Spaces & Mission Control |
| [§21](#21-notifications--focus-modes) | Notifications & Focus modes |
| [§22](#22-app-icon--dock) | App icon & Dock |
| [§23](#23-app-intents--shortcuts) | App Intents & Shortcuts on Mac |
| [§24](#24-performance--promotion) | Performance & ProMotion |
| [§25](#25-distribution-app-store-vs-developer-id--sparkle) | Distribution — App Store vs Developer ID + Sparkle |
| [§26](#26-the-mac-polish-checklist) | The Mac polish checklist |
| [§27](#27-anti-patterns) | Anti-patterns |

---

## 1. Window architecture

The window is the unit of a Mac app. Get this right and the rest follows.

### Window sizes

| Window | Default min size | Use |
| --- | --- | --- |
| Main app window | 1000 × 700pt | Most apps; supports sidebar + content + detail |
| Compact app window | 720 × 480pt | Utility apps, single-purpose tools |
| Inspector / floating | 360 × 600pt | Side panel for properties, drawn alongside main |
| Settings window | 580 × 420pt (varies by panel content) | Settings with `.commands` integration |
| About panel | 400 × 480pt (system-default size for `orderFrontStandardAboutPanel`) | Use the system about panel — don't roll your own |

```swift
WindowGroup(id: "main") {
    ContentView()
}
.defaultSize(width: 1100, height: 720)
.windowResizability(.contentMinSize)  // resize down to min content size, not arbitrarily small
.windowToolbarStyle(.unified)          // modern look — toolbar shares title bar
```

### Traffic lights (close / minimize / zoom)

The three colored dots in the top-left are NOT decoration — they're part of macOS muscle memory.

Rules:
- **Never hide them.** A Mac app without traffic lights feels broken.
- **Default position is correct.** Don't move them just to be different.
- **Custom positioning** is acceptable for unique layouts (e.g., Arc Browser's sidebar — they shift down 8pt because the sidebar starts at top):

```swift
.windowStyle(.hiddenTitleBar)  // hides default title, you draw your own
.toolbar(.hidden, for: .windowToolbar)
```

For most apps, use `.windowToolbarStyle(.unified)` — the toolbar shares the title bar area, traffic lights live at the natural top-left, the title text floats inline.

### Title bars

Three styles:

| Style | When |
| --- | --- |
| `.windowToolbarStyle(.unified)` | DEFAULT for modern Mac apps — toolbar + title share one bar (like Notes, Mail) |
| `.windowToolbarStyle(.unifiedCompact)` | Smaller variant — tighter vertical space (like Reminders) |
| `.windowStyle(.hiddenTitleBar)` | Hide the title bar entirely; you draw all chrome (Arc, some games) |

For Codex-style AI apps: `.unified` is right. Sidebar starts below the title bar; content scrolls behind it with material translucency.

### Window restoration

Mac users expect: close the app, reopen it, everything is exactly where they left it. The same windows, the same content, the same scroll positions.

In SwiftUI, use `@SceneStorage` for view-level state and `@AppStorage` for cross-window state:

```swift
struct ContentView: View {
    @SceneStorage("selectedItemID") var selectedItemID: String?
    @SceneStorage("sidebarVisible") var sidebarVisible: Bool = true
    @AppStorage("preferredColorScheme") var preferredColorScheme: ColorSchemePreference = .system

    var body: some View {
        NavigationSplitView(columnVisibility: $sidebarVisible) {
            sidebar
        } content: {
            content
        } detail: {
            detail
        }
    }
}
```

For UIKit/AppKit-based apps: implement `NSWindowRestoration` and `NSUserActivity` for full restoration.

### Minimum window size — math, not guess

The min size is calculated:
```
min width  = sidebar(220) + content(min 400) + detail(min 380) = 1000pt
min height = title bar(28) + content(min 600) + safe-area(12) = 640pt
```

Use `.navigationSplitViewColumnWidth(min: 200, ideal: 220, max: 320)` to constrain each column.

---

## 2. The sidebar pattern

The sidebar is THE Mac convention. Mail, Notes, Reminders, Finder, Music, Photos, Calendar, Linear, Things 3, Granola, Codex — they all use it. If your app shows lists, hierarchy, or navigation, it should have a sidebar.

### `NavigationSplitView` — the SwiftUI primitive

```swift
NavigationSplitView {
    SidebarView(selectedItemID: $selectedItemID)
} content: {
    if let item = selectedItem {
        ItemListView(parentID: item.id)
    } else {
        Text("Select a section")
            .foregroundStyle(.tertiary)
    }
} detail: {
    if let detailItem = selectedDetailID {
        ItemDetailView(itemID: detailItem)
    } else {
        Text("Select an item")
            .foregroundStyle(.tertiary)
    }
}
.navigationSplitViewStyle(.balanced)  // or .prominentDetail
```

### Sidebar dimensions

| Property | Value |
| --- | --- |
| Width | 200–240pt (220 is the sweet spot) |
| Min | 180pt |
| Max | 320pt |
| Row height | 24pt for default, 28pt for content-heavy rows |
| Internal horizontal padding | 8pt (rows extend to sidebar edges) |
| Section header padding | 12pt top, 4pt bottom |

### Sidebar typography

| Element | Font | Weight | Size | Color |
| --- | --- | --- | --- | --- |
| Section header (ALL CAPS) | SF Pro Text | `.semibold` | 11pt | `.secondary`, tracking 1.4 |
| Row label | SF Pro Text | `.regular` | 13pt | `.primary` |
| Selected row label | SF Pro Text | `.semibold` | 13pt | `.white` (on accent bg) |
| Counter badge | SF Pro Text | `.medium` | 11pt | `.secondary` |
| Inactive section badge | SF Pro Text | `.regular` | 11pt | `.tertiary` |

### Sidebar icons

- 16pt SF Symbol, `.symbolRenderingMode(.hierarchical)`
- 8pt gap between icon and label
- Selected row: icon stays the same color (white on accent bg) — DON'T change weight; that causes layout shift

```swift
Label("Inbox", systemImage: "tray.fill")
    .symbolRenderingMode(.hierarchical)
    .font(.system(size: 13))
```

### Selection styling

```swift
List(selection: $selectedID) {
    ForEach(sections) { section in
        Section(section.title.uppercased()) {
            ForEach(section.items) { item in
                NavigationLink(value: item.id) {
                    Label(item.title, systemImage: item.icon)
                }
            }
        }
    }
}
.listStyle(.sidebar)
```

The `.sidebar` list style gives you the proper Mac translucent material background, hover states, and selection coloring. **DO NOT** roll your own list styling for sidebars — `listStyle(.sidebar)` is correct.

### Hover states

```swift
.background(isHovered ? Color(NSColor.controlBackgroundColor).opacity(0.6) : Color.clear)
.onHover { hovering in
    isHovered = hovering
}
```

But `.listStyle(.sidebar)` does this for free — only add custom hover for custom-built lists.

### Type-to-select

A Mac convention that Mac apps rarely implement but ALL good ones do: typing characters jumps to the matching list item. Mail, Finder, and Linear all support this.

For `List`s in SwiftUI, this is automatic on `selection:`-driven lists. For custom lists, implement key handling via `.focusable()` + `.onKeyPress`.

### Drag-to-reorder

```swift
.onMove { from, to in
    items.move(fromOffsets: from, toOffset: to)
}
```

For `List`, this works automatically. For custom sidebars, implement `.draggable` + `.dropDestination`.

### Right-click context menu

Every sidebar row should support right-click for contextual actions:

```swift
.contextMenu {
    Button("Rename", action: rename).keyboardShortcut(.return, modifiers: [])
    Button("Duplicate", action: duplicate).keyboardShortcut("d", modifiers: .command)
    Divider()
    Button("Delete", role: .destructive, action: delete).keyboardShortcut(.delete, modifiers: [])
}
```

### Reference apps

- **Apple Mail**: the canonical sidebar. Mailboxes, smart folders, account hierarchy. Study how disclosure indicators work, how section headers behave, how unread counts align.
- **Linear**: workspaces / teams / projects in sidebar with collapsible sections.
- **Things 3**: areas + projects with elegant nesting.
- **Granola**: meetings list as sidebar, transcripts in content, AI notes in detail.
- **OpenAI Codex**: conversations + project pinned items. Sidebar collapses with `Cmd-Option-S`.

---

## 3. Toolbars

The toolbar is the persistent action surface at the top of your window. In macOS 13+, it integrates with the title bar in `.unified` style — the modern default.

### Item placement

```swift
.toolbar {
    ToolbarItemGroup(placement: .navigation) {
        Button(action: back) { Image(systemName: "chevron.left") }
        Button(action: forward) { Image(systemName: "chevron.right") }
    }

    ToolbarItem(placement: .principal) {
        SearchField()
            .frame(width: 280)
    }

    ToolbarItemGroup(placement: .primaryAction) {
        Button(action: share) { Image(systemName: "square.and.arrow.up") }
        Button(action: settings) { Image(systemName: "gearshape") }
    }
}
```

| Placement | Use |
| --- | --- |
| `.navigation` | Back/forward, source-list buttons |
| `.principal` | Centered title or search field |
| `.primaryAction` | Right-side primary actions (new, share, account) |
| `.automatic` | System-chosen position |
| `.cancellationAction` | Cancel for sheets (top-left in modal context) |
| `.confirmationAction` | OK/Save for sheets (top-right) |

### Icon style

- 16pt SF Symbol at `.semibold` weight
- `.symbolRenderingMode(.hierarchical)` for depth
- 8pt horizontal padding around each item
- 4pt internal padding for clickable area

### Search in the toolbar

A Mac convention: search lives in the toolbar, centered or right-aligned. Use `.searchable(text:)` which automatically places it in the toolbar:

```swift
NavigationSplitView { ... }
    .searchable(text: $query, placement: .toolbar, prompt: "Search messages")
```

This gives you `Cmd-F` to focus the search field for free.

### Hide on scroll (for immersive content)

For content-focused apps (writing, reading, watching), hiding the toolbar on scroll feels great:

```swift
.toolbar(scrollUp ? .visible : .hidden, for: .windowToolbar)
```

Don't overuse — most apps want a persistent toolbar.

---

## 4. The menu bar

A Mac app without a meaningful menu bar feels half-finished. Even single-purpose utilities should have File / Edit / View / Window / Help.

### Standard menus (in order)

1. **App menu** (`AppName`) — auto-populated by system. Adds your app name + standard items.
2. **File** — New, Open, Save, Close, Print, Export
3. **Edit** — Undo, Redo, Cut, Copy, Paste, Select All, Find
4. **View** — Show/Hide Sidebar, Show/Hide Toolbar, Zoom, View Modes
5. **Window** — Minimize, Zoom, Bring All to Front, [list of open windows]
6. **Help** — Search, Help Book

For specific app types, add: **Format** (text editors), **Run** / **Build** (dev tools), **Account** (apps with auth).

### SwiftUI `.commands {}`

```swift
@main
struct CodexApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
            .commands {
                CommandGroup(replacing: .newItem) {
                    Button("New Conversation") { newConversation() }
                        .keyboardShortcut("n", modifiers: .command)
                    Button("New Project") { newProject() }
                        .keyboardShortcut("n", modifiers: [.command, .shift])
                }
                CommandGroup(after: .sidebar) {
                    Button("Toggle Inspector") { toggleInspector() }
                        .keyboardShortcut("i", modifiers: [.command, .option])
                }
                CommandMenu("Code") {  // Custom menu
                    Button("Run") { run() }.keyboardShortcut("r", modifiers: .command)
                    Button("Stop") { stop() }.keyboardShortcut(".", modifiers: .command)
                }
            }
    }
}
```

### Menu item rules

- **Every item has a keyboard shortcut** unless it's something users will never use frequently (like "About").
- **Use system-standard shortcuts**: `Cmd-N` (new), `Cmd-O` (open), `Cmd-S` (save), `Cmd-W` (close window), `Cmd-Q` (quit), `Cmd-,` (settings).
- **NEVER reassign system shortcuts** to non-standard actions.
- **Capitalize titles**: "New Document" not "new document" — Mac convention is title case.
- **Use ellipsis (`…`)** when a menu item opens a dialog: "Open…", "Save As…", "Find…".
- **Group with dividers**: separators between logical groups.

### Disable items contextually

Menu items should disable when their action is unavailable:

```swift
Button("Save", action: save)
    .keyboardShortcut("s", modifiers: .command)
    .disabled(!hasUnsavedChanges)
```

Disabled items still appear in menus — they just gray out. This communicates "this exists, but isn't applicable right now."

### Reference: Apple Mail's menu bar

Study Apple Mail's full menu hierarchy on your own Mac. Every action you might want is in there. Every item has a shortcut. Every group is separated with dividers. That's the bar.

---

## 5. Keyboard shortcuts & focus

Mac is a keyboard machine. The minimum bar:

| Action | Shortcut | Always? |
| --- | --- | --- |
| New | `⌘N` | Yes |
| New Window | `⌘⇧N` | Multi-window apps |
| Open | `⌘O` | Document apps |
| Save | `⌘S` | Document apps |
| Save As… | `⌘⇧S` | Document apps |
| Close window | `⌘W` | Yes |
| Close tab (if tabbed) | `⌘W` | Tabbed apps |
| Close ALL windows | `⌘⌥W` | Multi-window apps |
| Quit | `⌘Q` | Yes |
| Undo | `⌘Z` | Editable content |
| Redo | `⌘⇧Z` | Editable content |
| Cut / Copy / Paste | `⌘X` / `⌘C` / `⌘V` | Editable content |
| Select All | `⌘A` | Lists, text |
| Find | `⌘F` | Anything searchable |
| Settings | `⌘,` | Yes |
| Toggle sidebar | `⌘⌥S` | Sidebar apps |
| Toggle inspector | `⌘⌥I` | Inspector apps |
| Command palette | `⌘K` | Modern AI/productivity apps |
| Quick switcher | `⌘P` (or `⌘O` if not used for Open) | Project/file apps |
| Toggle full-screen | `⌃⌘F` | Most apps |
| Hide app | `⌘H` | System-provided |
| Hide others | `⌘⌥H` | System-provided |

### `.keyboardShortcut` in SwiftUI

```swift
Button("New", action: createNew)
    .keyboardShortcut("n", modifiers: .command)

Button("Toggle Sidebar", action: toggleSidebar)
    .keyboardShortcut("s", modifiers: [.command, .option])
```

### Focus management

Use `@FocusState` to programmatically focus inputs:

```swift
enum Field: Hashable { case search, content, title }

@FocusState private var focusedField: Field?

TextField("Search", text: $query)
    .focused($focusedField, equals: .search)

// Focus on appear:
.onAppear { focusedField = .search }
```

### Tab navigation

Mac users press `Tab` to move between interactive elements. SwiftUI handles this automatically for `Button`, `TextField`, `Picker`, etc. For custom views, use `.focusable()`.

### Type-to-select

A Mac convention many apps miss. Typing characters with a list focused should jump to the matching item. SwiftUI's `List` does this automatically when bound to `selection:`.

### Number-key shortcuts for tabs/views

For apps with a small number of major views (Tabs 1-9):

```swift
.keyboardShortcut("1", modifiers: .command)  // First tab
.keyboardShortcut("2", modifiers: .command)  // Second tab
// ... etc
```

### Spacebar for primary preview action

Mac users press Space to toggle preview of selected list items (Finder's Quick Look pattern). Replicate for media-list apps.

---

## 6. The command palette (Cmd-K)

The modern AI/productivity Mac app pattern: `⌘K` opens a searchable command palette. Raycast popularized it. Linear, Things 3, Notion, OpenAI Codex, Granola all use it.

### What goes in the palette

- Every menu-bar action (so users can find any action)
- Recently-used items (recent files, conversations, notes)
- Quick filters / searches
- Settings actions
- Help / docs

### SwiftUI implementation pattern

```swift
@State private var paletteVisible = false

ContentView()
    .keyboardShortcut("k", modifiers: .command)
    .sheet(isPresented: $paletteVisible) {
        CommandPaletteView()
            .frame(width: 640, height: 480)
    }
    .background(
        Button("", action: { paletteVisible = true })
            .keyboardShortcut("k", modifiers: .command)
            .hidden()
    )
```

A more elegant approach: use a custom `NSPanel`-based overlay that floats above the window, centered, with a backdrop blur. This is what Raycast and Linear do.

### Palette design

- **Width**: 640pt (most apps)
- **Height**: 480pt with results, ~96pt collapsed (just search field)
- **Background**: thick material backdrop
- **Search field**: 22pt SF Pro Text, regular weight, no border, large placeholder
- **Result rows**: 36pt tall, icon + label + keyboard shortcut hint right-aligned
- **Result groups**: section headers between groups (Files, Actions, Settings)
- **Selected result**: accent color background, white text
- **Arrow keys**: navigate; `Return`: execute; `Esc`: dismiss

### Fuzzy search

Standard fuzzy search algorithm (the same one VS Code, Sublime, Raycast use): characters in order, scoring favors consecutive matches and matches at word starts.

Don't roll your own — use [`fuzzysearch-swift`](https://github.com/sgr-ksmt/FuzzySearch-swift) or similar.

### Reference

OpenAI Codex's `Cmd-K` palette is the modern reference. Linear's `Cmd-K` is the most feature-rich. Raycast IS the palette — study how they make it feel weightless.

---

## 7. Mouse, trackpad & hover states

Mac users move the mouse to discover. Every clickable element should respond to hover.

### `.onHover` in SwiftUI

```swift
@State private var isHovered = false

Button(action: { ... }) { ... }
    .onHover { hovering in
        isHovered = hovering
    }
    .background(isHovered ? Color.gray.opacity(0.1) : Color.clear)
    .animation(.easeOut(duration: 0.12), value: isHovered)
```

### Hover state rules

| Element | Default | Hover |
| --- | --- | --- |
| Sidebar row | clear | `.label.opacity(0.06)` background |
| List row | clear | `.label.opacity(0.04)` background |
| Toolbar icon button | clear | `.label.opacity(0.08)` circular bg |
| Card / tile | regular border | subtle scale (1.01) + slightly darker shadow |
| Inline link | underline none | underline appears |
| Tappable image | none | dim to 0.92 opacity OR show overlay |

**Hover animations** should be FAST (0.10–0.15s `.easeOut`) so they feel responsive. Slow hover transitions feel laggy.

### Cursor changes

Use `NSCursor` for context-appropriate cursors:

```swift
.onHover { hovering in
    if hovering {
        NSCursor.pointingHand.push()
    } else {
        NSCursor.pop()
    }
}
```

Or use the SwiftUI `.pointerStyle()` modifier (macOS 14+):

```swift
.pointerStyle(.link)  // hand cursor
.pointerStyle(.horizontalText)  // I-beam
.pointerStyle(.frameResize(.bottomLeading))  // resize cursor
```

### Trackpad gestures

| Gesture | What it does |
| --- | --- |
| Two-finger scroll | Scroll content |
| Pinch | Zoom (where applicable) |
| Two-finger swipe left/right | Back/forward navigation |
| Three-finger swipe up | Mission Control |
| Three-finger swipe down | App Exposé |
| Four-finger swipe up | Mission Control (default) |
| Force Touch (older trackpads) | Quick Look, deep dictionary lookup |

For navigation back/forward in apps with history:
```swift
.gesture(
    DragGesture(minimumDistance: 50)
        .onEnded { value in
            if value.translation.width > 50 { navigateBack() }
            else if value.translation.width < -50 { navigateForward() }
        }
)
```

### Right-click vs control-click

**Both should work.** Right-click is the modern convention. Control-click is the legacy fallback for users on devices without right-click. SwiftUI's `.contextMenu` handles both automatically.

---

## 8. Context menus (right-click)

Right-click context menus are the Mac equivalent of iOS long-press context menus, but with stricter conventions.

```swift
.contextMenu {
    Button("Open in New Window", action: openInNewWindow)
        .keyboardShortcut("o", modifiers: [.command, .shift])
    Button("Rename", action: rename)
    Button("Duplicate", action: duplicate)
        .keyboardShortcut("d", modifiers: .command)
    Divider()
    Menu("Share") {
        Button("Copy Link", action: copyLink)
        Button("Email", action: emailShare)
    }
    Divider()
    Button("Delete", role: .destructive, action: delete)
        .keyboardShortcut(.delete, modifiers: [])
}
```

### Rules

1. **Mirror menu-bar items** where applicable (Rename, Delete, Duplicate live in both places).
2. **Keyboard shortcuts displayed**: SwiftUI shows the `⌘D` hint automatically next to items that have `.keyboardShortcut`.
3. **Max 8 top-level items**. Use submenus for more.
4. **Destructive items last, with role: .destructive** (renders in red).
5. **Dividers between logical groups**.
6. **No icons in menu items** unless they communicate the action clearly (and even then, sparingly).

### Custom previews

```swift
.contextMenu {
    // menu items
} preview: {
    // SwiftUI preview shown above the menu
    Image(item.thumbnail)
        .resizable()
        .scaledToFit()
        .frame(width: 320, height: 200)
}
```

Finder, Photos, and Mail all do this — long-press on a file shows a preview alongside the menu.

---

## 9. Multi-window & document architecture

Mac apps support multiple windows naturally. This is a fundamental difference from iOS.

### Document-based apps (`NSDocument` / `DocumentGroup`)

```swift
@main
struct MyDocumentApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { file in
            DocumentView(document: file.$document)
        }
        .commands {
            // additional commands
        }
    }
}
```

This gives you:
- Auto-Save / Versions
- Drag-from-Finder open
- Recent Documents in File menu
- New Window from File menu
- Each document in its own window

### Non-document apps (`WindowGroup`)

```swift
@main
struct CodexApp: App {
    var body: some Scene {
        WindowGroup("Conversations", id: "main") {
            MainView()
        }

        WindowGroup("Project", for: Project.ID.self) { $projectID in
            ProjectWindow(projectID: projectID)
        }
        .windowResizability(.contentMinSize)

        Settings {
            SettingsView()
        }
    }
}
```

This lets you open additional windows programmatically:

```swift
@Environment(\.openWindow) private var openWindow

Button("Open Project") {
    openWindow(id: "project", value: project.id)
}
```

### Auxiliary windows (Inspector, Library)

For palette/inspector windows that float alongside the main window:

```swift
Window("Inspector", id: "inspector") {
    InspectorView()
}
.windowResizability(.contentSize)
.windowLevel(.floating)  // stays above main window
```

### Tab support

```swift
.windowsToolbarStyleManagedRefactored()  // older API
```

Mac's native window tabbing (the Cmd-T behavior) is automatic for `DocumentGroup`s. Users get tabbed windows for free.

For non-document apps, opt in via Window scene options.

### Window restoration

Apps using `WindowGroup` get restoration of *open windows* automatically. State within each window (scroll position, selection) requires `@SceneStorage` (see §1).

---

## 10. Status bar & MenuBarExtra utilities

For apps that live in the menu bar (Bartender, 1Password mini, Raycast, Karabiner): use `MenuBarExtra`.

```swift
@main
struct UtilityApp: App {
    var body: some Scene {
        MenuBarExtra("My Utility", systemImage: "circle.dashed") {
            MenuBarContent()
        }
        .menuBarExtraStyle(.window)  // or .menu
    }
}
```

| Style | Behavior |
| --- | --- |
| `.menu` | Standard NSMenu — appears as native dropdown menu |
| `.window` | Custom SwiftUI view appears in a popover-style panel |

### Status item icon

- **Always a template image** (`.template`) — system tints it for light/dark menu bar, accessibility settings.
- **22pt × 22pt** size on standard menu bar, 44×44 in Big Sur+ supports larger.
- **No color** — template images are monochrome silhouettes.

Create your icon as a black-on-transparent PNG and tag it as a template:

```swift
NSImage.Name("status-icon")  // Asset Catalog → mark as Template
```

### Show / Hide on click

```swift
@State private var showingPopover = false

MenuBarExtra("My Utility", systemImage: "circle.dashed") {
    PopoverContent()
        .frame(width: 320, height: 480)
}
.menuBarExtraStyle(.window)
```

The system handles opening/closing automatically with `.menuBarExtraStyle(.window)`.

### Apps that demonstrate this well

- **Raycast**: the entire app lives in the menu bar (and via global hotkey)
- **Bartender**: organizes the menu bar itself
- **1Password mini**: quick-access vault from menu bar
- **Cleanshot X**: screenshot tools from menu bar
- **Mosaic / Magnet**: window management from menu bar

---

## 11. Liquid Glass on macOS (Tahoe / macOS 26)

macOS 26 (Tahoe) brought Liquid Glass to the Mac. Sidebars, toolbars, dock, and many system surfaces now use the new translucent material.

### Adopting Liquid Glass

Most Liquid Glass adoption is automatic — using semantic SwiftUI APIs picks it up:

```swift
// Sidebar — Liquid Glass automatic on macOS 26
.listStyle(.sidebar)

// Toolbar — Liquid Glass automatic with .unified style
.windowToolbarStyle(.unified)

// Container background
.background(.bar)              // toolbar-like material
.background(.regularMaterial)  // standard frosted
.background(.thickMaterial)    // more opaque
```

For custom views that want Liquid Glass:

```swift
.glassEffect()                                      // default — regular variant
.glassEffect(.regular.tint(.accentColor))           // tinted glass
.glassEffect(.regular.interactive())                // tap response
.glassEffect(.regular, in: .rect(cornerRadius: 12)) // custom shape
```

### Rules for Liquid Glass on Mac

1. **Glass for floating controls only** — toolbar items, dock-style buttons. Don't make whole content areas glass; users need a solid reading surface.
2. **Tint primary actions sparingly** — see iOS skill for the "tint one thing per screen" rule. Same applies.
3. **Test in both modes** — Liquid Glass renders differently against light backgrounds vs dark vs colorful wallpapers. Check all three.
4. **Reduce Transparency**: when the user has Reduce Transparency on (Accessibility), the system falls back to opaque automatically. You don't need to handle this — but DO test it.
5. **Don't add Liquid Glass to your app icon** — that's the system's job.

### Pre-Tahoe fallback

If your minimum target is macOS 14 or 15:

```swift
@ViewBuilder
func adaptiveBackground() -> some View {
    if #available(macOS 26.0, *) {
        Color.clear.glassEffect(.regular.interactive())
    } else {
        Color.clear.background(.regularMaterial)
    }
}
```

---

## 12. Typography on Mac

Mac typography is mostly the same as iOS (SF Pro family), but with different density expectations.

### System font sizes

Mac uses larger UI font sizes than you might expect:

| Element | Size | Weight |
| --- | --- | --- |
| Window title | 13pt | `.semibold` |
| Sidebar row | 13pt | `.regular` |
| List row primary | 13pt | `.regular` |
| List row secondary | 11pt | `.regular`, secondary color |
| Toolbar button label | 11pt | `.semibold` (rare — usually icon-only) |
| Body text in content | 14pt | `.regular` |
| Reading text in long-form content | 15-17pt | `.regular` |
| Hero numbers / stats | 28-48pt | `.bold` rounded |
| Code (inline + blocks) | 13pt | `.regular` SF Mono |
| Settings label | 13pt | `.regular` |
| Settings help text | 11pt | `.regular`, secondary |

### SF Mono is critical for code apps

```swift
Text(codeSnippet)
    .font(.system(size: 13, design: .monospaced))
```

Or set the font once via `.font(.body.monospaced())`.

For full code editor experiences: ship a custom monospaced font (Berkeley Mono, JetBrains Mono, IBM Plex Mono) bundled with your app. Codex uses a custom monospace font.

### Mac-specific Dynamic Type

Mac doesn't have full iOS-style Dynamic Type, but it does honor "Larger Text" accessibility setting. Use semantic font styles (`.body`, `.callout`, `.caption`) so the system handles scaling.

### Tabular numerals for changing numbers

```swift
Text("\(count)").font(.body.monospacedDigit())
```

For dashboards, timers, prices — same rule as iOS.

---

## 13. Color & material

The color rule from the iOS polish skill applies on Mac too: **pick in OKLCH, ship in Display P3**. Mac displays (especially Pro Display XDR) often have wider gamut than iPhones — P3 colors render even more vividly.

### Semantic Mac colors

| Token | Use |
| --- | --- |
| `Color(.controlBackgroundColor)` | Standard control background |
| `Color(.windowBackgroundColor)` | Window background (regions outside content) |
| `Color(.underPageBackgroundColor)` | Translucent material backings |
| `Color(.textBackgroundColor)` | Text fields, scrollable text |
| `Color(.controlAccentColor)` | User's accent color (System Settings) |
| `Color(.selectedTextBackgroundColor)` | Selected text highlight |
| `Color(.gridColor)` | Subtle list dividers |
| `Color(.separatorColor)` | Standard separators |

### Materials

| Material | Use |
| --- | --- |
| `.ultraThinMaterial` | Very translucent — for floating overlays |
| `.thinMaterial` | Toolbar / sidebar fills |
| `.regularMaterial` | Standard panel backgrounds |
| `.thickMaterial` | More opaque, for sheets |
| `.bar` | Title bar / toolbar material (matches system) |

### Vibrancy

Vibrancy (the color-shifting effect over translucent materials) is automatic when you use semantic colors atop SwiftUI materials. If you hard-code colors over `.regularMaterial`, vibrancy is lost.

### Mac-specific accent handling

Users can change their system accent color in System Settings. Mac apps should respect this via `Color.accentColor`. If your app has a brand color you want to enforce, use a custom named asset that explicitly opts out:

```swift
Color("BrandBlue")  // doesn't follow system accent
```

But for most controls, `.tint(.accentColor)` is correct.

---

## 14. Spacing & density

Mac apps can be denser than iOS apps because users have bigger screens AND precise pointing. But density without rhythm is chaos.

### Mac spacing scale (4pt grid)

| Spacing | Use |
| --- | --- |
| 2pt | Hairlines, sub-row separators |
| 4pt | Tight icon-text gap, intra-row vertical |
| 8pt | Standard small gap, list-item internal padding |
| 12pt | Card internal padding, default vertical rhythm |
| 16pt | Content padding (window content edges) |
| 20pt | Section spacing |
| 24pt | Larger section spacing |
| 32pt | Group separation |
| 48pt+ | Marketing-like screens, hero spacing |

### Content padding

- **Window edges**: 20pt horizontal, 16pt vertical for content areas
- **Sidebar**: rows extend edge-to-edge (no horizontal padding); 8pt vertical between sections
- **Content area between sidebar and detail**: 16pt padding around grouped content
- **Detail pane**: 20pt around content
- **Inspector**: 12pt around content (tighter — it's a side panel)

### Sidebar density

Default `.listStyle(.sidebar)` row heights are 24pt for short rows, 28pt for content-heavy. Don't go below 22pt — accessibility and target size both suffer.

---

## 15. Drag and drop

Mac users expect drag-and-drop *everywhere*: sidebar reordering, dragging files into the app, dragging items out to Finder, dragging between windows.

### `.draggable` and `.dropDestination`

```swift
Text(item.title)
    .draggable(item)  // item conforms to Transferable
```

```swift
.dropDestination(for: Item.self) { items, location in
    for item in items { handleDrop(item) }
    return true
}
```

### `Transferable` conformance

```swift
struct Conversation: Transferable {
    let id: UUID
    let title: String
    let messages: [Message]

    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .conversation)
        ProxyRepresentation(exporting: \.title)  // for text-based drops
    }
}

extension UTType {
    static var conversation = UTType(exportedAs: "com.heyimjames.codex.conversation")
}
```

### Drag previews

```swift
.draggable(item) {
    // Preview shown during drag
    HStack {
        Image(systemName: "doc")
        Text(item.title)
    }
    .padding(8)
    .background(.regularMaterial, in: .rect(cornerRadius: 8))
}
```

### Drop indicators

For dropping into a list-of-items pane, show a 2pt accent-colored line at the drop position:

```swift
@State private var dropTarget: Int? = nil

.dropDestination(for: Item.self) { items, location in
    // ...
} isTargeted: { targeted in
    dropTarget = targeted ? computeDropIndex(location) : nil
}
```

Render the indicator line between rows at `dropTarget`.

### Drag from Mac to Finder

For apps that produce files (PDFs, images, exports), `.draggable` with a file Transferable representation allows the user to drag the item to Finder, the desktop, or another app:

```swift
.draggable(generateFile())  // returns a FileRepresentation
```

---

## 16. Code-app specifics — syntax highlighting, monospace, terminals

For apps in the Codex / Cursor / VS Code space — AI coding tools, dev tools, code editors.

### Syntax highlighting

Three options:

1. **TreeSitter** (`TreeSitterClient` Swift wrapper): incremental parsing, fast, used by serious editors. Setup is involved.
2. **[Splash](https://github.com/JohnSundell/Splash)** by John Sundell: pure Swift, smaller scope (Swift-only by default, extensible). Good for Swift-specific tools.
3. **Highlight.js via WebView**: hack, but easy. Embed Highlight.js in a WKWebView. Works for all languages.

For a Codex-quality app, TreeSitter is correct.

### Code block UI

| Element | Spec |
| --- | --- |
| Font | SF Mono or bundled monospace (Berkeley, JetBrains) at 13pt |
| Background | `Color(.textBackgroundColor).opacity(0.5)` over material |
| Padding | 12pt all sides for blocks; 4pt vertical 6pt horizontal for inline |
| Corner radius | 8pt for blocks; 4pt for inline |
| Line height | 1.4 × font size |
| Language label | Top-right, 11pt, secondary color |
| Copy button | Top-right or hover-only; SF Symbol `doc.on.doc` |

### Code block component example

```swift
struct CodeBlock: View {
    let code: String
    let language: String
    @State private var isHovered = false
    @State private var copied = false

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            HStack {
                Text(language)
                    .font(.system(size: 11, weight: .medium))
                    .foregroundStyle(.secondary)
                Spacer()
                if isHovered {
                    Button(action: copy) {
                        Image(systemName: copied ? "checkmark" : "doc.on.doc")
                            .contentTransition(.symbolEffect(.replace))
                    }
                    .buttonStyle(.plain)
                    .help(copied ? "Copied" : "Copy")
                }
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(Color(.textBackgroundColor).opacity(0.4))

            Text(highlightedCode)
                .font(.system(size: 13, design: .monospaced))
                .textSelection(.enabled)
                .padding(12)
                .frame(maxWidth: .infinity, alignment: .leading)
        }
        .background(Color(.textBackgroundColor).opacity(0.3))
        .clipShape(.rect(cornerRadius: 8))
        .onHover { isHovered = $0 }
    }

    private func copy() {
        NSPasteboard.general.clearContents()
        NSPasteboard.general.setString(code, forType: .string)
        copied = true
        Task {
            try? await Task.sleep(for: .seconds(1.5))
            copied = false
        }
    }
}
```

### Inline code

```swift
Text("Run `npm install` to set up dependencies.")
```

For markdown-style auto-formatting, use `AttributedString` parsing or a markdown rendering library.

### File trees

For project navigation:
- **Disclosure rows** with `>` indicator that rotates 90° on expand
- **File-type icons** via Apple's NSWorkspace API: `NSWorkspace.shared.icon(forFile: path)`
- **Indent per level**: 16pt
- **Right-click context menu**: New File, New Folder, Reveal in Finder, Delete

```swift
struct FileTreeRow: View {
    let url: URL
    @State private var isExpanded = false
    @State private var children: [URL] = []

    var body: some View {
        DisclosureGroup(isExpanded: $isExpanded) {
            ForEach(children, id: \.self) { child in
                FileTreeRow(url: child)
            }
        } label: {
            HStack(spacing: 6) {
                Image(nsImage: NSWorkspace.shared.icon(forFile: url.path))
                    .resizable()
                    .frame(width: 16, height: 16)
                Text(url.lastPathComponent)
                    .font(.system(size: 13))
            }
        }
        .onAppear { loadChildren() }
    }

    private func loadChildren() {
        children = (try? FileManager.default.contentsOfDirectory(at: url, includingPropertiesForKeys: nil)) ?? []
    }
}
```

### Embedded terminals

For dev tools that need shell integration:

1. **Display only** (read-only output): embed `NSTextView` in a SwiftUI view, append output as it streams from a `Process`.
2. **Full PTY** (interactive terminal): use Apple's [`SwiftTerm`](https://github.com/migueldeicaza/SwiftTerm) library. It handles VT100 escape codes, color, cursor positioning.

For Codex-style apps where the AI runs commands and shows output, the read-only pattern is usually right. Full PTY is heavier and only needed for full terminal emulators.

### Code diffs

Side-by-side or unified diff renderings need:
- **Green background** (`Color(.systemGreen).opacity(0.15)`) for added lines
- **Red background** (`Color(.systemRed).opacity(0.15)`) for removed lines
- **Gray + line number** for context
- **Same monospaced font** as code blocks
- **Sticky line numbers** in the gutter

---

## 17. Settings window

Mac settings live in a separate window opened via `Cmd-,` — not a sheet, not a sidebar item.

### `Settings` scene in SwiftUI

```swift
@main
struct CodexApp: App {
    var body: some Scene {
        WindowGroup { ... }
        Settings {
            TabView {
                GeneralSettingsView()
                    .tabItem { Label("General", systemImage: "gear") }
                AccountSettingsView()
                    .tabItem { Label("Account", systemImage: "person.circle") }
                AdvancedSettingsView()
                    .tabItem { Label("Advanced", systemImage: "slider.horizontal.3") }
            }
            .frame(minWidth: 580, idealWidth: 640, minHeight: 420)
        }
    }
}
```

### Settings window design rules

1. **Tabs at the top** (NOT a sidebar) — Mac Settings convention since System Settings redesign.
2. **Each tab has its own content** — keep heights similar across tabs so the window doesn't jump on tab switch (or use `.frame(minHeight:)` to enforce consistent sizing).
3. **Right-aligned controls, left-aligned labels** — standard Mac form layout.
4. **Section headers in small caps** (12pt semibold).
5. **Help text below related controls** in 11pt secondary color.
6. **No "Save" button** — settings persist on change. Use `@AppStorage` to bind.
7. **No "Close" or "Done" button** — users dismiss with the window close button.

### Settings form layout

```swift
Form {
    Section("Appearance") {
        Picker("Theme:", selection: $theme) {
            Text("System").tag(Theme.system)
            Text("Light").tag(Theme.light)
            Text("Dark").tag(Theme.dark)
        }
        Toggle("Use vibrant sidebar", isOn: $vibrantSidebar)
    }

    Section {
        Toggle("Show line numbers", isOn: $showLineNumbers)
        Toggle("Show whitespace", isOn: $showWhitespace)
    } header: {
        Text("Editor")
    } footer: {
        Text("Whitespace characters render as light gray dots.")
            .font(.caption)
            .foregroundStyle(.secondary)
    }
}
.formStyle(.grouped)
.padding()
```

`.formStyle(.grouped)` gives you the native Mac System Settings look — sectioned cards with light fills.

---

## 18. About, Help, & App Shortcuts

### About panel

Use the system about panel — don't roll your own:

```swift
.commands {
    CommandGroup(replacing: .appInfo) {
        Button("About \(Bundle.main.appName)") {
            NSApplication.shared.orderFrontStandardAboutPanel(
                options: [
                    NSApplication.AboutPanelOptionKey.credits: NSAttributedString(string: "Made with care in [City] by [Author]"),
                    NSApplication.AboutPanelOptionKey.applicationName: "Codex",
                    NSApplication.AboutPanelOptionKey.applicationVersion: appVersion,
                    NSApplication.AboutPanelOptionKey(rawValue: "Copyright"): "© 2026 [Author]"
                ]
            )
        }
    }
}
```

For something more polished: custom About window via a `Window` scene with an opt-in design.

### Help menu

The Help menu lives in the menu bar between Window and the right edge.

- **Search field at top** — system-provided
- **Custom help items** below

```swift
CommandGroup(replacing: .help) {
    Button("Codex Help") { openHelp() }
    Button("Keyboard Shortcuts") { showShortcuts() }
        .keyboardShortcut("?", modifiers: .command)
    Divider()
    Button("Send Feedback…") { sendFeedback() }
}
```

For full help docs: ship an Apple Help Book bundle (`.help`). It's involved — most apps just point to web docs.

### App Shortcuts (Spotlight + Shortcuts.app)

Expose your app's actions to Spotlight, Shortcuts app, and Siri via `AppIntents`:

```swift
import AppIntents

struct NewConversationIntent: AppIntent {
    static var title: LocalizedStringResource = "Start a new conversation"
    static var openAppWhenRun = true

    func perform() async throws -> some IntentResult {
        await AppState.shared.newConversation()
        return .result()
    }
}

struct CodexShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: NewConversationIntent(),
            phrases: ["Start a new conversation in \(.applicationName)"],
            shortTitle: "New Conversation",
            systemImageName: "message"
        )
    }
}
```

Now your action is invocable via:
- Spotlight (`Cmd-Space` then start typing)
- Shortcuts app
- Siri ("Hey Siri, start a new conversation in Codex")
- Apple Watch (via Shortcuts)

---

## 19. Spotlight, Quick Look & Continuity

### Spotlight integration

Index your app's content for Spotlight via `CoreSpotlight`:

```swift
import CoreSpotlight
import CoreServices

func indexConversation(_ conversation: Conversation) {
    let attrs = CSSearchableItemAttributeSet(contentType: .conversation)
    attrs.title = conversation.title
    attrs.contentDescription = conversation.summary
    let item = CSSearchableItem(uniqueIdentifier: conversation.id.uuidString, domainIdentifier: "conversations", attributeSet: attrs)
    CSSearchableIndex.default().indexSearchableItems([item])
}
```

Now users can search for conversations in Spotlight. Tapping the result opens your app to that conversation (via `NSUserActivity` handling).

### Quick Look

For apps that show files (images, PDFs, code files): press Space on a selected item to show Quick Look preview.

```swift
.fileImporter(...) { ... }
.quickLookPreview($previewURL)
```

Or implement a custom `QLPreviewProvider` for app-specific data types.

### Continuity (Handoff)

Let users start in your Mac app, continue on iPhone (or vice versa).

```swift
.userActivity("com.codex.conversation", isActive: currentConversation != nil) { activity in
    activity.title = currentConversation?.title ?? "Codex"
    activity.userInfo = ["conversationID": currentConversation?.id.uuidString ?? ""]
}
.onContinueUserActivity("com.codex.conversation") { activity in
    if let id = activity.userInfo?["conversationID"] as? String {
        openConversation(id: id)
    }
}
```

When the user has your Mac app open with a conversation, the icon appears in their iPhone's app switcher with a Handoff badge. Tap to continue on iPhone.

### Universal Control

Universal Control lets users drag between Mac and iPad. It works automatically for `.draggable` items that are `Transferable`. No additional work needed.

### Shared with You

If your app receives links shared via Messages on Mac, surface them in a "Shared with You" section:

```swift
import SharedWithYou

class SharedLinkCenter: NSObject, SWHighlightCenterDelegate {
    func highlightCenterHighlightsDidChange(_ center: SWHighlightCenter) {
        // surface center.highlights in your UI
    }
}
```

---

## 20. Stage Manager, Spaces & Mission Control

Mac windows participate in Stage Manager, Spaces, and Mission Control automatically. You don't need to do anything special — but you should make sure your windows behave well:

### Stage Manager behaviors

- Each `Window` / `WindowGroup` is its own Stage Manager window.
- Avoid auxiliary "panel" windows that don't belong in Stage Manager — use `Settings { ... }` for settings (which is excluded automatically) and `.windowLevel(.floating)` for floating panels.
- Stage Manager auto-arranges windows by size; design for ~75% screen width as a "comfortable" Stage Manager size.

### Mission Control thumbnails

When Mission Control activates, your windows are rendered as thumbnails. Avoid pure-dark UIs with no chrome — they're hard to distinguish in Mission Control thumbnails. Even a small toolbar or title gives the thumbnail a visual anchor.

### Spaces

Users can pin your windows to specific Spaces. You don't control this — but you should test that your app behaves correctly when its window is in a non-active Space (e.g., notifications don't bring it forward unexpectedly).

---

## 21. Notifications & Focus modes

### `UNUserNotificationCenter`

Same API as iOS:

```swift
let center = UNUserNotificationCenter.current()
try await center.requestAuthorization(options: [.alert, .sound, .badge])

let content = UNMutableNotificationContent()
content.title = "New message from Codex"
content.body = "Your generation is complete."
content.sound = .default
content.interruptionLevel = .active  // .passive, .active, .timeSensitive, .critical

let request = UNNotificationRequest(identifier: UUID().uuidString, content: content, trigger: nil)
try await center.add(request)
```

### Communication Notifications

For chat-style apps, use Communication Notifications (avatars on Lock Screen + Notification Center). See [chat-and-messaging skill](../chat-and-messaging/SKILL.md) for full pattern.

### Notification timing

Mac users have multiple displays, often multiple Macs, often multiple devices. Notifications should:
- **Only fire for genuinely important events** — a background task completing, an incoming message, a critical error
- **Never fire for routine app state** — saves, autosaves, opening a file
- **Respect Focus mode** — automatic via `interruptionLevel`

### App Dock badge

For unread counts or pending notifications:

```swift
NSApplication.shared.dockTile.badgeLabel = "\(unreadCount)"
```

To remove: set to `nil` or empty string. **Use sparingly** — a permanent dock badge with no real meaning is annoying.

### Dock icon bouncing

NEVER programmatically bounce the dock icon. It's reserved for "you have unread messages" and similar. The system manages this for you when notifications fire.

---

## 22. App icon & Dock

Mac app icons are NOT iOS app icons. They follow different conventions.

### The icon template

- **1024 × 1024 base**, then downscaled to 512, 256, 128, 64, 32, 16
- **Squircle shape** — but content extends to the rounded edges (unlike iOS where icons fill the rounded square)
- **Tilted / 3D / illustrative** — Mac icons traditionally use depth, shadows, perspective. The "flat square" iOS style looks out of place on Mac.
- **Recognizable at 16pt** — icons appear in Spotlight, menus, Finder. Test the smallest size.

### Icon variants

Use Asset Catalog with macOS app icon set:
- All sizes from 16 to 1024 with @1x and @2x for each

Apple's "App Icon Composer" doesn't exist anymore — use the Asset Catalog wizard in Xcode or generate from a single 1024 master with [`iconutil`](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Optimizing/Optimizing.html#//apple_ref/doc/uid/TP40012302-CH7-SW3).

### Reference icons to study

- **Codex** — the OpenAI logo treated as a Mac icon (subtle depth, recognizable mark)
- **Linear** — the L mark with subtle gradient depth
- **Things 3** — the iconic checkbox with depth and shadow
- **Granola** — the bowl icon with realistic shading
- **Mail / Notes / Reminders** — Apple's first-party icons set the gold standard for skeuomorphic-but-modern style

### Dock customization

You can customize the dock icon at runtime for state changes:

```swift
NSApp.applicationIconImage = NSImage(named: "AppIcon-Recording")  // shows recording state
```

Use sparingly — the dock icon should mostly stay as your brand icon.

### Dock menu

Right-click your app's dock icon to show a custom menu:

```swift
class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDockMenu(_ sender: NSApplication) -> NSMenu? {
        let menu = NSMenu()
        menu.addItem(withTitle: "New Conversation", action: #selector(newConversation), keyEquivalent: "")
        menu.addItem(withTitle: "Recent: Project A", action: #selector(openRecent), keyEquivalent: "")
        return menu
    }
}
```

---

## 23. App Intents & Shortcuts

Mac apps benefit from App Intents same as iOS — expose actions to Shortcuts, Spotlight, and Siri. See §18 for the AppShortcuts pattern.

### Mac-specific intents

- **Open project** — let users open a specific project from Shortcuts
- **Search content** — let Shortcuts query your app's data
- **Generate report** — long-running task surfaced to Shortcuts

### Focus filters

```swift
import AppIntents

struct CodexFocusFilter: SetFocusFilterIntent {
    static var title: LocalizedStringResource = "Codex Focus Filter"

    @Parameter(title: "Hidden Projects")
    var hiddenProjects: [Project]

    func perform() async throws -> some IntentResult {
        // Hide specified projects during this Focus mode
        return .result()
    }
}
```

Users see your filter in System Settings → Focus → [Mode] → Apps. They configure which projects to hide during Work focus, for example.

---

## 24. Performance & ProMotion

Mac displays run from 60Hz (built-in MacBook Air, Mac mini) up to 120Hz ProMotion (MacBook Pro, Pro Display XDR).

### Frame-rate targets

- **60fps minimum** on all displays
- **120fps target** on ProMotion displays for smooth animations

### Optimize for ProMotion

```swift
// Use CADisplayLink for tight animations
class AnimationDriver {
    private var displayLink: CADisplayLink?
    func start() {
        displayLink = CADisplayLink(target: self, selector: #selector(tick))
        displayLink?.preferredFrameRateRange = CAFrameRateRange(minimum: 60, maximum: 120, preferred: 120)
        displayLink?.add(to: .main, forMode: .common)
    }
    @objc private func tick() {
        // update animation
    }
}
```

### Heavy rendering off-main-thread

For syntax highlighting, code parsing, AI streaming, file processing — never on main thread. Use `Task.detached` or `DispatchQueue.global()`:

```swift
.task {
    let highlighted = await Task.detached {
        return await syntaxHighlighter.highlight(code, language: lang)
    }.value
    self.highlightedCode = highlighted
}
```

### Lazy rendering

`LazyVStack` / `LazyHStack` / `LazyVGrid` for large lists. Don't render off-screen content.

For chat-style streaming UIs: virtualize messages. Only render visible + buffer.

### Instruments — profile early

Use Xcode's Instruments (Time Profiler, Allocations, Animation Hitches) on your slowest device. The lowest-end MacBook Air should still hit 60fps.

---

## 25. Distribution — App Store vs Developer ID + Sparkle

### App Store

Pros: easier user trust (Apple-signed), automatic updates, integrated payment / subscriptions, family sharing.
Cons: 30% (or 15%) revenue cut, App Store sandboxing requirements, slower review, restricted APIs.

### Developer ID (direct distribution)

Pros: full API access, no sandbox required (but supported), no revenue cut, fast iteration, you control update channel.
Cons: must use Sparkle (or similar) for updates, must notarize every release, must convince users to install outside MAS.

### Notarization

Required regardless of distribution channel:

```bash
xcrun notarytool submit MyApp.dmg --keychain-profile "AC_PASSWORD" --wait
xcrun stapler staple MyApp.dmg
```

Without notarization, macOS shows a scary "App is damaged" warning on first open.

### Sparkle for auto-updates (non-MAS)

[Sparkle](https://sparkle-project.org) is the de-facto auto-update framework for Mac apps outside the App Store.

```swift
import Sparkle

@main
struct CodexApp: App {
    private let updaterController = SPUStandardUpdaterController(startingUpdater: true, updaterDelegate: nil, userDriverDelegate: nil)

    var body: some Scene {
        WindowGroup { ContentView() }
            .commands {
                CommandGroup(after: .appInfo) {
                    CheckForUpdatesView(updater: updaterController.updater)
                }
            }
    }
}

struct CheckForUpdatesView: View {
    @ObservedObject private var checkForUpdatesViewModel: CheckForUpdatesViewModel
    private let updater: SPUUpdater

    init(updater: SPUUpdater) {
        self.updater = updater
        self.checkForUpdatesViewModel = CheckForUpdatesViewModel(updater: updater)
    }

    var body: some View {
        Button("Check for Updates…", action: updater.checkForUpdates)
            .disabled(!checkForUpdatesViewModel.canCheckForUpdates)
    }
}
```

### Hardened runtime

Required for notarization. Enable in Xcode → Project → Signing & Capabilities → Hardened Runtime.

Then carefully audit your entitlements — only enable what you actually need.

### Sandboxing (required for MAS)

MAS apps must opt into App Sandbox. This restricts file access, network access, etc.

For Codex-style AI apps that need to read project files, write to user-selected directories, run shell commands — sandboxing is restrictive. Direct distribution often makes more sense.

---

## 26. The Mac polish checklist

Run this before considering ANY Mac app done.

### Window
- [ ] Window has proper minimum size set
- [ ] Traffic lights at default position (or intentionally repositioned)
- [ ] `.windowToolbarStyle(.unified)` for modern look
- [ ] Window restoration works (close + reopen restores state)
- [ ] All windows have meaningful titles

### Sidebar
- [ ] `.listStyle(.sidebar)` for native sidebar appearance
- [ ] Section headers in small caps, secondary color
- [ ] Hover states on rows (automatic with `.sidebar` style)
- [ ] Type-to-select works
- [ ] Drag-to-reorder works (if applicable)
- [ ] Right-click context menu on every row

### Toolbar
- [ ] `.toolbar` populated with relevant actions
- [ ] Icons use SF Symbols with `.symbolRenderingMode(.hierarchical)`
- [ ] Search via `.searchable` if applicable
- [ ] `Cmd-F` focuses search

### Menu bar
- [ ] All standard menus present (File, Edit, View, Window, Help)
- [ ] Every meaningful action has a `.keyboardShortcut`
- [ ] No reassigned system shortcuts
- [ ] Disabled items disable correctly (not hidden)
- [ ] Ellipsis on items that open dialogs

### Keyboard
- [ ] `Cmd-N` (new), `Cmd-O` (open), `Cmd-S` (save) all wired
- [ ] `Cmd-,` opens Settings
- [ ] `Cmd-W` closes window
- [ ] `Cmd-Q` quits
- [ ] `Cmd-Z` / `Cmd-Shift-Z` for undo/redo where applicable
- [ ] `Cmd-K` opens command palette
- [ ] `Cmd-1` through `Cmd-9` for tab/view switching
- [ ] Tab navigation through interactive elements works
- [ ] Spacebar previews selected list items (where applicable)

### Mouse / trackpad
- [ ] Hover states on EVERY clickable element
- [ ] Cursor changes appropriately (`.pointerStyle()`)
- [ ] Right-click context menus everywhere they make sense
- [ ] Two-finger scroll works in all scrollable areas
- [ ] Two-finger swipe back/forward in nav-history apps

### Settings
- [ ] Lives in `Settings { ... }` scene (opens via `Cmd-,`)
- [ ] Tabs at top (not sidebar)
- [ ] Settings persist via `@AppStorage` — no Save button needed
- [ ] Help text below related controls
- [ ] Sections with headers / dividers

### About / Help
- [ ] About panel uses system `orderFrontStandardAboutPanel`
- [ ] Help menu populated
- [ ] Credits include a personal touch ("Made with care in [City]")

### Distribution
- [ ] App is notarized
- [ ] Hardened runtime enabled
- [ ] If using Sparkle: appcast URL configured, EdDSA signing key created
- [ ] If MAS: sandbox entitlements audited

### Liquid Glass (macOS 26+)
- [ ] Sidebar uses `.listStyle(.sidebar)` (auto-Liquid Glass)
- [ ] Toolbar uses `.windowToolbarStyle(.unified)`
- [ ] Custom floating overlays use `.glassEffect()`
- [ ] Tested with Reduce Transparency (Accessibility)

### Accessibility
- [ ] All interactive elements have meaningful `.accessibilityLabel`
- [ ] VoiceOver announces all state changes
- [ ] Increase Contrast tested
- [ ] Full Keyboard Access tested
- [ ] Reduce Motion tested

### Code-app specifics (if applicable)
- [ ] SF Mono or custom monospace font for code
- [ ] Syntax highlighting for primary languages
- [ ] Copy button on code blocks (hover-revealed)
- [ ] File tree with native file icons
- [ ] Diff rendering with green/red backgrounds

### The smile test
- [ ] Open the app, glance for 3 seconds — does it feel native? Does it feel Mac-y?
- [ ] If you've never used the app before, can you find the main action without thinking?
- [ ] If you close the app and reopen, is everything back exactly where you left it?

---

## 27. Anti-patterns

The things that signal "this is a web app pretending to be a Mac app" or "the developer doesn't use Macs":

1. **No menu bar items beyond the system defaults.** A Mac app without File / Edit / View / Window menus feels broken.
2. **Custom window controls (not traffic lights).** Even Slack figured this out eventually. Use the system traffic lights.
3. **No keyboard shortcuts on actions.** Every Mac user expects every meaningful button to also be a shortcut.
4. **Hover states missing on buttons.** Mac users move the mouse to discover. No hover = the button looks dead.
5. **Sidebar that doesn't use `.listStyle(.sidebar)`.** Custom-rolled sidebars look obviously not-Mac.
6. **Settings as a sheet inside the main window.** Settings is its own window, opened via `Cmd-,`.
7. **"Save" button in Settings.** Settings persist on change. Bind via `@AppStorage`.
8. **Window content that doesn't restore on relaunch.** Mac users expect "exactly where I left it."
9. **Wide UI density everywhere (iOS-padded).** Mac screens are big; respect density. iOS padding wastes screen.
10. **Right-click does nothing.** Every list, every cell, every actionable element should have a context menu.
11. **No `Cmd-K` command palette in 2026.** It's expected by users of modern Mac apps.
12. **Buttons too small for precise pointing.** Mac pointers are pixel-precise — but tap targets should still be reasonable (~24pt min).
13. **Custom blur effects instead of `.regularMaterial`.** The system handles vibrancy correctly; custom blur usually doesn't.
14. **Disabled buttons hidden instead of grayed out.** Mac convention: disabled items still appear in menus, just grayed.
15. **No window tabs.** Document-based apps get them for free via `DocumentGroup`. Other apps should opt in.
16. **`Cmd-F` doesn't focus search.** Search is `Cmd-F`. Make it so.
17. **Notifications for routine app state.** A notification for "Saved" or "Opened" is noise. Only notify for events the user cares about asynchronously.
18. **Dock bouncing programmatically.** The system handles this for notifications. Don't bounce manually.
19. **Sidebar items that show counts but don't update reactively.** Use `@Observable` / `@Published` and bind. Stale counts = broken-feeling.
20. **Multi-line text fields without `Cmd-Return` to submit.** Match Linear / iMessage / Slack conventions: `Return` adds newline, `Cmd-Return` submits.

---

## Final principles

1. **Mac is a real platform with real conventions.** Respect them. Code → menus, keyboard, sidebar, hover, right-click — those aren't optional, they're the contract with the Mac user.
2. **Keyboard-first; mouse-enhanced.** Every action has a shortcut. Every list has type-to-select. Every interactive element has Tab focus.
3. **The window is the unit.** Multi-window is natural. Window state restoration is mandatory.
4. **Restraint over decoration.** Liquid Glass is a system surface; your job is to put restrained content on it.
5. **OpenAI Codex is the modern reference** for AI-tool Mac apps. Linear, Things 3, Granola, Raycast are the reference for productivity Mac apps. Apple Mail / Notes / Finder are the reference for fundamentals.
6. **Test on the smallest target hardware.** A MacBook Air should hit 60fps. A Pro Display XDR should hit 120fps. The middle takes care of itself.

The benchmark: a Mac user uses your app for the first time, presses `Cmd-K` and finds it works. Presses `Cmd-,` and gets Settings. Closes the app and reopens — everything is back. They tell a friend: "It just feels right on Mac." That's the goal.

---

## Reference reading

- [Apple Human Interface Guidelines — macOS](https://developer.apple.com/design/human-interface-guidelines/macos)
- [Apple — App Menu](https://developer.apple.com/design/human-interface-guidelines/menus)
- [Apple — Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [Apple — Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
- [Apple — Keyboard shortcut conventions](https://support.apple.com/en-us/HT201236)
- [Sparkle Project](https://sparkle-project.org)
- [Designing for the Mac — WWDC](https://developer.apple.com/videos/play/wwdc2020/10104/)
- [What's New in SwiftUI for macOS — WWDC](https://developer.apple.com/videos/play/wwdc2024/10148/)

And the apps to study:
- **OpenAI Codex** — modern AI dev tool reference
- **Linear** — Mac-native productivity, command palette, keyboard-first
- **Things 3 (Mac)** — restraint, polish, masterclass in animation
- **Granola** — meeting-notes app, native Mac feel
- **Notion Calendar / Cron** — calendar app, polished Mac chrome
- **Raycast** — command palette as primary UI; menu bar utility done right
- **Arc Browser** — innovative tabs, sidebar-as-primary
- **Cursor** — code editor (Electron but mostly Mac-feeling)
- **Bear** — note-taking, beautiful typography
- **Tower** — Git client, deeply polished
- **Apple Mail / Notes / Reminders / Finder** — system reference for fundamentals
