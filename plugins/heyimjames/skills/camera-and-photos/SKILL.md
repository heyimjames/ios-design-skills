---
name: ios-camera-and-photos-design
description: "Design and build best-in-class native iOS camera, photo-capture, and photo-editing apps with the polish of Halide, Kino, Lapse, VSCO, and Apple Photos. Use this skill whenever the user is building, reviewing, or refining a SwiftUI/UIKit app that involves the camera, photo library, video capture, image editing, filters, scanning, AR effects, AI photo features, or anything backed by AVFoundation, PhotoKit, Vision, VisionKit, Core Image, ImageCaptureCore, ARKit, RoomPlan, or LiDAR. Triggers on: camera, viewfinder, shutter button, AVCaptureSession, AVCapturePhotoOutput, PHPicker, PhotoKit, photo library, photo grid, photo edit, filter, crop, presets, LUT, Cinematic mode, Portrait mode, ProRAW, ProRes, Live Photos, HDR, depth, LiDAR, subject lifting, VisionKit, Live Text, document scanner, QR scanner, magic eraser, object removal, AI photo, Core ML, Vision framework, ARKit face tracking, manual camera controls, Camera Control button, volume button shutter, spatial photo, spatial video, Apple Vision Pro."
metadata:
  short-description: Design native iOS camera, photo, and video apps with the polish of Halide, Lapse, and Apple Photos.
---

# iOS Camera & Photos — Design Engineering Skill

A taste guide for building camera and photo apps that feel like they were made by people who actually shoot photos. Every value in this file is opinionated and specific — pulled from studying flows on Mobbin and shipping native iOS apps.

## Output format — required

When this skill is invoked to review camera/photo code or recommend changes, **always output recommendations as a markdown table** with three columns:

| Before | After | What this changes |
| --- | --- | --- |
| The current code, value, or approach (quote the user's actual code when possible) | The recommended replacement — **specific**, with exact values | One sentence on what the user will *see, feel, or experience* differently |

Three rules:
1. **Before** quotes the user's actual code where possible.
2. **After** is specific. Exact pt values, exact haptic styles, exact API calls.
3. **What this changes** is *experiential or visual*, not abstract.

Output ONE table with multiple rows for multi-recommendation reviews — not one table per row. Use `—` for Before if the user hasn't implemented that thing yet.

**Examples drawn from this skill:**

| Before | After | What this changes |
| --- | --- | --- |
| `Circle().frame(width: 80, height: 80)` as shutter | 76pt outer ring (4pt stroke) + 60pt inner fill with 4pt gap | Shutter reads as a real camera button instead of a generic dot — matches Apple Camera convention and signals "this app respects your craft" |
| `AVCapturePhotoOutput.capturePhoto(...)` fired on `.onEnded` (touch-up) | Fire on `.onChanged` (touch-down) with a prepared `.impact(weight: .light)` haptic | Capture latency drops from ~50ms to <5ms; the click feels mechanical instead of laggy — the moment is preserved |
| `Color(red: 1.0, green: 0.85, blue: 0.0)` (focus ring yellow) | `Color(.displayP3, red: 1.0, green: 0.85, blue: 0.0)` | Focus ring renders at full chroma on every Apple device since 2017 — chrome feels Halide-refined instead of generic-iOS |

This format is required for every recommendation output by this skill.

---

## Philosophy

> The camera is a feeling, not a feature.

Camera apps live or die in three places:
1. **The half-second between intent and capture.** From the moment a user lifts their phone to the moment the shutter fires, every frame of friction matters. The viewfinder must be live before the launch animation finishes. The shutter must respond on touch-down, not touch-up.
2. **The trust that the photo is *real*.** Manual controls, RAW capture, and visible depth/exposure data tell serious shooters this app respects their craft. Auto-everything tells casual shooters this app respects their time. Pick a side.
3. **The way the result *lands*.** A flash that's too aggressive, a thumbnail that pops in late, a haptic that fires too soon — all of these break the spell. The capture confirmation is the most important moment in the whole product.

The pixel-pushers' rules:
- **The shutter button is sacred.** Never reuse that visual language for anything else.
- **Black is your canvas.** True black (`#000000`), not "almost black." OLED loves it. Photos look better against it. Don't fight this.
- **The viewfinder is full-bleed.** Controls overlay; they don't crop the frame. If you must crop, dim the cropped area but still show it (Apple Camera's "Show Outside Frame" pattern).
- **No skeuomorphism unless you go ALL the way.** (Not Boring) Camera is excellent because it commits. Half-realistic dials look like a student project.

## Reference apps to study

When in doubt, copy. These are the apps you should be benchmarking against, with the specific flows worth lifting:

| App | What to learn from it | Mobbin flow |
| --- | --- | --- |
| **Apple Photos** | Library pinch-zoom across grid sizes, hero transition into single photo, edit toolbar (Adjust/Filters/Crop) with a slider that detents at neutral | [Editing a photo](https://mobbin.com/flows/da47b2da-f094-46b9-9760-90bc109d948e), [Zooming in](https://mobbin.com/flows/1dbf59e9-f687-4387-9207-f3b4ac9a5c68), [Library](https://mobbin.com/flows/20451a7a-5e55-476e-aa07-0a0e074ad1b5) |
| **Halide / Kino (Lux)** | Manual focus dial with peaking overlay, all-thumb-zone controls, OLED-black chrome, RAW/ProRAW toggles, video grade selector | [Adjusting manual focus](https://mobbin.com/flows/df9bf3e3-da23-4c7d-b127-be69a25029d2), [Adjusting white balance](https://mobbin.com/flows/4a025179-242d-4cf7-9988-95eb03bdbb53) |
| **VSCO** | Filter strip with named presets, before/after long-press, "Studio" mounting board for in-progress edits, tool tray | [Applying a preset](https://mobbin.com/flows/eb662391-0dc2-4fb2-be6c-ceeb814c534a), [Editing skew](https://mobbin.com/flows/0ef61ad2-4a90-47f7-aed5-6a66a09dfea6), [Retro filter](https://mobbin.com/flows/f13060a7-bd87-4aa0-957a-5dbbcdfe2719) |
| **Lapse** | Wait-as-feature ("develop in 6 hours"), single-tap capture w/ no preview, animated archive flick, collaborative rolls | [Developing snaps](https://mobbin.com/flows/62c2320a-80ba-4c1e-8458-1e04d3f41f92), [Creating a camera roll](https://mobbin.com/flows/092746dd-dba6-4a89-af7e-9f2f756709bc) |
| **Locket** | "Send to friend" as the entire reason the camera exists; no library, no edit, no scroll — just capture-and-send | [Camera](https://mobbin.com/flows/a16e33e2-501a-4c26-ac00-ab960e345040) |
| **(Not Boring) Camera** | Skeuomorphism done with conviction — wood textures, knurled dials, exposure meter that *moves*, every control physical | [Taking a photo](https://mobbin.com/flows/5c3e02e1-7660-44cc-a912-735bd3369eae) |
| **Google Photos** | Magic Eraser / circle-to-erase, AI Enhance suggestions tile, AutoFrame crop, square/portrait quick toggle | [Cropping](https://mobbin.com/flows/567234a4-4792-43bc-a450-5e70f09da68b), [Filter w/ slider](https://mobbin.com/flows/cc011f03-5e95-4f5a-a816-a8dc0a1e8965) |
| **Instagram (Stories editor)** | Filter wash with named strength slider ("Fade warm — 50"), modular tool tray (Audio/Text/Overlay/Filter/Edit) | [Adding a filter](https://mobbin.com/flows/7fbb1069-6478-4c25-bf9f-8d2c9864b5b3) |
| **Riveo** | Creative effect timeline with keyframes, VHS/scanline aesthetics, layered effect mixing | [Add effect adjustment](https://mobbin.com/flows/fcea9439-c8eb-4077-9dd4-9b510492726a) |
| **Google Arts & Culture** | AI-feature browser as a *play* surface (Art Selfie, Art Filter, Color Palette match) — playful, not utilitarian | [Camera](https://mobbin.com/flows/bcc65bf3-a27e-4a80-8a39-368177b81fc4) |

---

## Hero interactions — the moments that matter

### 1. Launching the camera

The viewfinder MUST be visible before the launch animation completes. This is non-negotiable.

```swift
// AVCaptureSession.startRunning() is BLOCKING and slow. Always:
// 1. Create the session and inputs on init() inside a background queue.
// 2. Attach the AVCaptureVideoPreviewLayer to the SwiftUI/UIKit view immediately.
// 3. Call startRunning() on a dedicated session queue, NOT main.
// 4. Use NotificationCenter.default to listen for .AVCaptureSessionDidStartRunning
//    and fade the viewfinder in only when frames are actually arriving.

let sessionQueue = DispatchQueue(label: "camera.session.queue", qos: .userInitiated)
sessionQueue.async { session.startRunning() }
```

Visual sequence:
- **0–80ms**: black viewfinder appears, chrome (shutter, flip button) fades in at `opacity 0→1` over 240ms with `.easeOut(duration: 0.24)`.
- **80–250ms**: first preview frame arrives. Cross-fade from black to live (`opacity 0→1` over 160ms, `.linear`).
- **250ms+**: chrome is fully visible, viewfinder is live, AF/AE has converged.

Anti-pattern: showing a placeholder/blurred image during launch. Just hold black. It feels more intentional.

### 2. The shutter button

This is the most important component in the entire app. Treat it that way.

**Geometry:**
- Outer ring: 76pt diameter, 4pt stroke, white at 100% opacity.
- Inner fill: 60pt diameter, white, gap of 4pt between fill and ring.
- For video mode: inner fill morphs from circle (60pt) → rounded rect (30pt × 30pt, 6pt corner radius) → animated red. Use `withAnimation(.spring(response: 0.32, dampingFraction: 0.7))` for the shape morph.
- For "burst": long-press grows the inner fill to 64pt and pulses subtly.

**Interaction:**
| State | Visual | Haptic | Timing |
| --- | --- | --- | --- |
| Touch-down (photo) | Inner fill scales to 0.88 | `UIImpactFeedbackGenerator(style: .light)` prepared in advance, `.impactOccurred()` on touch-down | < 16ms (1 frame) |
| Touch-up (photo) | Inner fill scales back to 1.0 with spring overshoot to 1.04 then settle | `UIImpactFeedbackGenerator(style: .medium).impactOccurred()` simultaneously with `AVCapturePhotoOutput.capturePhoto(...)` call | spring(response: 0.28, dampingFraction: 0.55) |
| Capture confirm | Full-screen white flash overlay, opacity 0 → 0.85 → 0 over 180ms with `.easeOut` | optional `UINotificationFeedbackGenerator().notificationOccurred(.success)` for "shot saved" — but ONLY after the photo is committed to PhotoKit, not before | 180ms total |
| Video start | Inner morphs to red rounded-rect, outer ring pulses (1.0 → 1.05 → 1.0 every 1.2s) | `.medium` impact once on start | morph 320ms |
| Video stop | Inner morphs back to circle | `.light` impact | morph 280ms |

**Critical detail**: capture should fire on touch-DOWN for serious camera apps (Halide, Kino) so the moment is preserved. Apple Camera fires on touch-UP to avoid accidental shots — pick based on your audience.

**Volume buttons as shutter**: Use `AVCaptureEventInteraction` (iOS 17.2+) for the modern way. On older OS, observe `AVSystemController_SystemVolumeDidChangeNotification` (private but tolerated for camera apps) or use `MPVolumeView` interception. Halide and Kino do this — it's the difference between feeling like a real camera and feeling like a toy.

**iPhone 16 Camera Control button**: Implement `AVCaptureEventInteraction` and observe `AVCaptureControl` for half-press (focus lock) and full-press (capture). The half-press haptic is system-provided — don't try to fake it.

### 3. Focus & exposure tap

Tapping the viewfinder is the single most discoverable action in the app.

```swift
// 80pt yellow square, 2pt stroke, no fill, centered on the tap point.
// Animates: opacity 0 → 1 (80ms), scale 1.4 → 1.0 (220ms ease-out cubic),
// then "lock" pulse: scale 1.0 → 0.94 → 1.0 (320ms) with .selectionChanged haptic.
// After 1.4s of inactivity: opacity 1 → 0 over 320ms.

let focusIndicator = UIView()
focusIndicator.frame = CGRect(x: 0, y: 0, width: 80, height: 80)
focusIndicator.layer.borderColor = UIColor.systemYellow.cgColor
focusIndicator.layer.borderWidth = 2
focusIndicator.center = tapLocation
```

**Drag-to-expose** (Apple's "sun" gesture):
- After the focus square appears, a vertical slider (the "sun" icon) appears beside it.
- Drag up = increase EV (brighter), drag down = decrease.
- Range: ±2 EV by default.
- Haptic `.soft` every 0.5 EV crossed.
- Haptic `.rigid` at the 0 EV detent (back to neutral).
- The sun icon rotates 0–360° proportional to EV adjustment as you drag — a tiny detail that signals "you're touching the dial".

**Long-press on viewfinder = AE/AF lock** (Apple convention):
- Yellow banner slides down from top: "AE/AF LOCK" — 6pt vertical padding, 12pt horizontal, yellow background, black text.
- Spring in/out with `.spring(response: 0.36, dampingFraction: 0.82)`.
- Tap anywhere to release.

### 4. Mode switcher (Photo / Video / Portrait / ...)

The horizontal scrolling pill is the iOS-native pattern (Apple Camera). Don't reinvent.

```swift
// Use SwiftUI ScrollView with paging + snap, OR a custom UIScrollView
// with paging set per "page width" = single label width + spacing.
// Critical: the SELECTED mode is always at the SAME on-screen X position
// (typically dead-center). The list scrolls UNDER a fixed selection indicator.

ScrollView(.horizontal, showsIndicators: false) {
    HStack(spacing: 28) {
        ForEach(modes) { mode in
            Text(mode.title.uppercased())
                .font(.system(size: 13, weight: .semibold, design: .default))
                .tracking(1.2)
                .foregroundStyle(mode.id == selected ? .yellow : .white.opacity(0.6))
                .contentTransition(.interpolate)
                .id(mode.id)
        }
    }
    .padding(.horizontal, screenWidth / 2 - estimatedLabelHalfWidth)
}
.scrollTargetBehavior(.viewAligned) // iOS 17+
.onChange(of: selected) { _, _ in
    UISelectionFeedbackGenerator().selectionChanged()
}
```

Specs:
- Label spacing: 28pt between centers (NOT 28pt gap — center-to-center, which means rendering at consistent visual rhythm).
- Selected: bright accent (yellow for Apple-feel, app-tint for branded) + 110% font weight via `.font(.semibold)`.
- Unselected: 60% white opacity.
- Haptic: `.selectionChanged` on each detent crossing (NOT on every pixel — debounce to detent transitions).
- Haptic intensity: subtle. Use `UISelectionFeedbackGenerator`, not impact. Mode switching shouldn't feel like a hammer.

### 5. Pinch to zoom

A camera that can't zoom feels broken.

- Use `UIPinchGestureRecognizer` on the preview view.
- Map pinch scale to camera zoom factor with **logarithmic** interpolation (not linear) — zoom is a perceptual log scale.
- Show a circular indicator: ring with current zoom factor in the center (e.g., "1.4×"). Position: center of the viewfinder, fades in at the start of the pinch, fades out 600ms after release.
- Discrete zoom buttons (0.5×, 1×, 2×, 5×) at the bottom: tapping snaps with a 240ms spring; pinching through them triggers `.soft` haptic at each detent.
- ProMotion (120Hz) devices: update zoom on `CADisplayLink` for smoothness.

```swift
do {
    try device.lockForConfiguration()
    device.videoZoomFactor = clamp(newFactor, device.minAvailableVideoZoomFactor,
                                              device.maxAvailableVideoZoomFactor)
    device.unlockForConfiguration()
} catch { /* handle */ }

// For ultra-smooth zoom transitions across optical lenses (0.5x → 1x → 2x):
device.ramp(toVideoZoomFactor: target, withRate: 8.0) // rate in factors-per-second
```

### 6. Capture confirmation

The thumbnail-flying-to-corner animation is iconic. Here's how to nail it:

1. **Flash overlay** (180ms): full-screen white, `opacity 0 → 0.85 → 0`, `.easeOut`.
2. **Thumb materializes** (in parallel, starting at 60ms into the flash): a thumbnail of the just-captured photo appears at the *exact pixel size of the final viewfinder-fill*, full opacity, center of screen.
3. **Hero flight** (380ms, starting at 120ms): the thumbnail scales from full-frame down to ~48pt and translates to the gallery button position. Use `matchedGeometryEffect` in SwiftUI or a `UIView.transition(...)` with custom timing.
4. **Gallery button bumps** when the thumbnail arrives: scale 1.0 → 1.18 → 1.0 over 280ms with bounce. Quick `.soft` haptic.

```swift
.matchedGeometryEffect(id: "capturedPhoto", in: namespace)
.transition(.asymmetric(
    insertion: .scale(scale: 1.0).combined(with: .opacity),
    removal: .identity
))
.animation(.spring(response: 0.38, dampingFraction: 0.82), value: showingThumb)
```

**The signature detail: the spinner travels.** Adapted from Family's design philosophy — if a brief "saving" indicator appears after capture, it must NOT sit at the shutter. It migrates to where the result will appear: ON the gallery button, the same spot the thumbnail will land. The user's eye follows one location, not two. Apply this everywhere: save → progress migrates to the album badge; export → migrates to the share button; sync → migrates to the library icon. Loading states travel to their destination.

### 7. Photo grid (library view)

Apple Photos' pinch-to-grid-size is the gold standard. Implement it.

Grid sizes (Apple Photos):
- **All Photos** (1pt gap, 5 columns): smallest, densest. Use for browsing huge libraries.
- **Days** (3 columns, smart-cropped). Faces and subjects get more area via Vision face detection.
- **Months** (1 large hero per month + smaller supporting tiles).
- **Years** (one tile per year, full-bleed).

The pinch transition between zoom levels is the magic. Implementation:

```swift
// Use a custom UICollectionViewTransitionLayout or, in SwiftUI 17+,
// matchedGeometryEffect across grid configurations.
// CRITICAL: when transitioning from N×N grid to (N±1)×(N±1) grid, each
// cell needs to map to a specific destination cell. Pre-compute this mapping
// before the animation starts.

UIView.animate(withDuration: 0.42,
               delay: 0,
               usingSpringWithDamping: 0.86,
               initialSpringVelocity: 0.4) {
    collectionView.setCollectionViewLayout(newLayout, animated: false)
} completion: { _ in /* ... */ }
```

Haptic: `UIImpactFeedbackGenerator(style: .soft).impactOccurred()` at each grid-size threshold during the pinch. The user feels "click, click, click" as they pinch through levels — even though the visual is fluid.

### 8. Single-photo viewer

When you tap a thumbnail, the experience should feel like physically picking up the photo.

- **Hero**: `matchedGeometryEffect` from the thumb cell to the full-screen image. Spring `.spring(response: 0.4, dampingFraction: 0.82)`.
- **Drag-to-dismiss**: vertical drag pulls the photo with rubber-banding. Background darkens with linear opacity tied to drag distance (0 → 200pt drag = 1.0 → 0 opacity). Release past 120pt OR with velocity > 600pt/s dismisses with a continuation of the velocity.
- **Pinch-to-zoom on photo**: max zoom = max(image.width / view.width, image.height / view.height) × 4. Below 1.0, photo snaps back. Above max, rubber-bands. Use `CADisplayLink` for buttery zoom on ProMotion.
- **Double-tap-to-zoom**: 1× ↔ 2×, with the zoom point centered on the tap location. Spring `.spring(response: 0.36, dampingFraction: 0.8)`.

### 9. Editing — adjustment sliders

The slider is where amateur photo apps die. Get this right:

**Geometry:**
- Track height: 2pt, white at 20% opacity (background); 100% opacity (filled portion to current value).
- Thumb: 24pt circle, white, with a 1pt subtle shadow (radius 4, opacity 0.18, y-offset 2).
- Tick marks: small vertical lines, 1pt wide × 6pt tall, white at 30% opacity, every 10 units across the range.
- Center detent at 0 (for adjustments that have a neutral): slightly larger tick (8pt tall), white 60% opacity.

**Range and behavior:**
- Range: −100 to +100 for most adjustments (exposure, contrast, saturation).
- For exposure specifically, prefer ±2 EV expressed in stops (−2.0 to +2.0).
- For temperature: 2000K to 10000K in Kelvin.
- Initial position: always neutral (0 for adjustments, AS-SHOT for white balance).

**Interaction:**
- Drag the thumb, drag anywhere on the track, OR drag anywhere on the photo (Apple Photos pattern — bonus discoverability).
- Live preview updates at 60fps (or 120fps on ProMotion). Use `CIContext` with `useSoftwareRenderer: false` and a `MTLDevice` to keep filtering on the GPU.
- Numeric readout appears above the thumb during drag: SF Mono, 13pt, white, with a small fillable pill background.
- Center detent magnetism: within ±3 of zero, snap to zero with `UIImpactFeedbackGenerator(style: .rigid).impactOccurred()`. This is THE detail people remember.
- Haptic `.soft` every 25 units crossed (for the −100…+100 range that's −75, −50, −25, +25, +50, +75).

**Before/after**:
- Long-press the photo (NOT the slider): shows the un-edited original. Top banner reads "ORIGINAL" in small caps. Release to return to the edited version.
- Animate the difference with a fast crossfade (`opacity 1 → 0` over 90ms) — don't morph the pixels.

### 10. Filter strip

Horizontal scrolling filter presets, each rendered as a tiny thumbnail of *the user's actual photo* (not a stock image) with the filter applied.

**Specs:**
- Cell: 64pt × 64pt thumb + label below (10pt SF, semibold, 1.0 tracking).
- Spacing: 12pt between cells.
- Selected cell: thumb scales to 1.06 with a 2pt yellow border + label color shifts to yellow. Spring `.spring(response: 0.32, dampingFraction: 0.78)`.
- Non-selected cells: thumb at 1.0, label at white 70%.
- Edge fade: 24pt linear gradient mask at the left/right edges so cells fade out as they leave the visible area.

**Generating thumbnails**: pre-render all filter previews on a background queue when the photo is first opened. Cache them. Don't generate on-the-fly during scroll.

**Intensity slider**: when a filter is selected, a horizontal slider appears below or above the filter strip. Default value is 100 (filter at full strength). Range 0–100. Crossfades the filter on/off via opacity blending — DON'T regenerate the filter at each step (too slow).

### 11. Crop tool

Crop is where most apps look amateur. Reference Apple Photos and Google Photos for this:

- 8 grabbers: 4 corners (24pt × 24pt L-shape outside the corner) + 4 edge midpoints (24pt × 4pt or 4pt × 24pt).
- Drag a corner: aspect ratio is free unless the user picked a constraint (Square, 4:3, 16:9, etc.).
- Drag an edge: changes only that dimension.
- Drag inside the crop: pans the image within the crop frame.
- Outside the crop: dimmed to 40% black overlay (NOT solid black — you want to show context).
- Grid overlay: rule-of-thirds (default), or golden-ratio, or square grid. Lines at 0.5pt, white 30% opacity.

**Straighten dial**:
- Below the crop area, a horizontal angle dial: degree marks every 1°, with major ticks at every 5°.
- The current angle reads out above the dial: "−2.4°" in SF Mono, 17pt, white.
- Haptic `.rigid` at each 0° crossing (back to level).
- Haptic `.soft` every 1° otherwise.
- Drag the dial to rotate the image; the image visually rotates around its center with `.linear` motion (no spring — feels too floaty for fine adjustment).

**Auto-straighten**: button that runs `VNDetectHorizonRequest` (Vision framework) on the image and snaps the dial to the correct angle. Animate the snap with `.spring(response: 0.42, dampingFraction: 0.85)`.

**Aspect ratio chips**: horizontal row of pills (Free, Square, 9:16, 4:3, 4:5, 16:9). Tapping a chip animates the crop frame to that aspect with spring `.spring(response: 0.36, dampingFraction: 0.82)`.

### 12. Subject lifting (iOS 16+)

The "lift a subject out of a photo" feature (VisionKit) is magical when it works. Implementation:

```swift
import VisionKit

// On the image view, attach an ImageAnalysisInteraction (UIKit) or
// ImageAnalyzer (SwiftUI) — long-press on a subject lifts it.

let analyzer = ImageAnalyzer()
let interaction = ImageAnalysisInteraction()
imageView.addInteraction(interaction)

let config = ImageAnalyzer.Configuration([.visualLookUp])
let analysis = try await analyzer.analyze(image, configuration: config)
interaction.analysis = analysis
interaction.preferredInteractionTypes = .imageSubject
```

UX:
- Long-press: subject's outline glows with a chasing-light shimmer (CAEmitterLayer or a custom Metal shader). This visual is iconic — replicate it carefully.
- Lift: the subject becomes a draggable PNG with transparency. Drop into another app via UIKit drag-and-drop.
- Save: option to save just the subject as a transparent PNG to Photos.

### 13. Magic erase / object removal

The Google Photos / Apple Photos "Clean Up" pattern:

- User taps "Erase" tool. The image dims slightly (8% black overlay) to signal mode.
- User brushes over the object with a finger; the brushed area fills with a soft pink/orange highlight (60% opacity) showing the inpainting mask.
- Release: ML model runs (on-device via Core ML if possible, or via your backend). A subtle shimmer animation runs across the masked area while the inpainting completes.
- Result fades in over 320ms.

Use Apple's on-device `ImagePlayground` API (iOS 18.2+) where possible, or fall back to a custom inpainting model trained on LaMa / Stable Diffusion inpainting weights.

### 14. Live Photos

If your app supports capture, supporting Live Photos is table stakes:

```swift
photoSettings.livePhotoMovieFileURL = livePhotoTempURL
photoSettings.livePhotoVideoCodecType = .hevc
```

In the library, indicate Live Photos with the LIVE badge (top-left), and play on long-press with a `PHLivePhotoView`. The play-on-press feel matters — use the system view; don't roll your own.

---

## Animation curves cheat sheet

These are the values I use across camera/photo apps:

| Surface | Curve | Notes |
| --- | --- | --- |
| Shutter press | `.spring(response: 0.18, dampingFraction: 0.6)` | Fast, slight overshoot — feels mechanical |
| Mode switch | `.snappy(duration: 0.28, extraBounce: 0.12)` | iOS 17+ `.snappy` is great here |
| Filter cell select | `.spring(response: 0.32, dampingFraction: 0.78)` | Subtle scale + border fade |
| Slider thumb | `.linear` | Sliders should NEVER spring — they fight your finger |
| Crop dial | `.linear` | Same as above |
| Hero (thumb → fullscreen) | `.spring(response: 0.4, dampingFraction: 0.82)` | The "iOS feel" default |
| Modal sheet | `.spring(response: 0.45, dampingFraction: 0.86)` | Slightly slower than hero |
| Capture flash | `.easeOut(duration: 0.18)` | Linear in/sharp out |
| Focus indicator pulse | `.easeOut(duration: 0.22)` | Single decisive contraction |
| Grid pinch | `.spring(response: 0.42, dampingFraction: 0.86)` | Heavier — moving lots of pixels |
| AE/AF lock banner | `.spring(response: 0.36, dampingFraction: 0.82)` | Standard slide-down |

**Reduce Motion accessibility**: when `UIAccessibility.isReduceMotionEnabled` is true:
- Replace springs with crossfades (0.2s `.easeInOut`).
- KILL the hero transitions — just hard-cut to the destination.
- Keep haptics; they're separate from motion settings.

---

## Haptics cheat sheet

| Action | Generator | Style | When to prepare? |
| --- | --- | --- | --- |
| Shutter touch-down | `UIImpactFeedbackGenerator` | `.light` | Prepare on touch-down; fire immediately |
| Capture commits | `UIImpactFeedbackGenerator` | `.medium` | Fire on `photoOutput(_:didFinishProcessingPhoto:)` |
| Save success | `UINotificationFeedbackGenerator` | `.success` | After PHAsset is created |
| Save error | `UINotificationFeedbackGenerator` | `.error` | On PhotoKit write failure |
| Mode switch | `UISelectionFeedbackGenerator` | `.selectionChanged` | Prepare when scroll starts |
| Filter selection | `UISelectionFeedbackGenerator` | `.selectionChanged` | Per-cell |
| Slider zero detent | `UIImpactFeedbackGenerator` | `.rigid` | One-shot |
| Slider quarter mark | `UIImpactFeedbackGenerator` | `.soft` | Throttle to one per 80ms |
| Zoom lens crossover (0.5×→1×→2×) | `UIImpactFeedbackGenerator` | `.soft` | One per crossover |
| Focus tap | `UISelectionFeedbackGenerator` | `.selectionChanged` | On tap |
| AE/AF lock engaged | `UINotificationFeedbackGenerator` | `.success` | One-shot |
| Burst capture (each frame) | `UIImpactFeedbackGenerator` | `.soft` | Throttle: max 8/sec |

**Critical rule**: ALWAYS call `.prepare()` on a feedback generator before you expect to use it. The latency between "fire" and "feel" is ~50ms otherwise. Prepared, it's < 5ms.

```swift
final class ShutterHaptics {
    private let light = UIImpactFeedbackGenerator(style: .light)
    private let medium = UIImpactFeedbackGenerator(style: .medium)

    func armForShot() {
        light.prepare()
        medium.prepare()
    }
    func touchDown() { light.impactOccurred() }
    func captured() { medium.impactOccurred() }
}
```

For ultra-custom haptics, use **CoreHaptics** with `CHHapticEngine` — you can choreograph multi-tap patterns (e.g., a "shutter then film advance" haptic that fires `.medium` followed by three `.soft` ticks 60ms apart, simulating a film advance). Halide does this on some captures and it's lovely.

---

## Typography for camera UIs

The wrong font wrecks the whole feel. Defaults that work:

| Surface | Font | Weight | Size | Tracking |
| --- | --- | --- | --- | --- |
| Mode labels | SF Pro / SF Compact | `.semibold` | 13pt | 1.2 (tracking applied as `.tracking()` modifier) |
| Numeric readouts (ISO, shutter, EV) | **SF Mono** | `.medium` | 13pt | 0 |
| Settings titles | SF Pro | `.regular` | 17pt | 0 |
| Album titles in library | SF Pro Rounded | `.bold` | 34pt (large title) → 17pt scrolled | 0 |
| Photo metadata (filename, date) | SF Pro | `.regular` | 13pt | 0 |
| Toast messages | SF Pro | `.medium` | 15pt | 0 |
| AE/AF LOCK banner | SF Pro | `.heavy` | 11pt UPPERCASE | 1.8 |

**Always use `SF Mono` for numeric overlays** that change rapidly (zoom factor, EV, shutter speed) — proportional digits jitter as values change, monospace stays rock-still.

---

## Color & material

- **True black** (`UIColor.black`) for camera chrome backgrounds — never `#1C1C1E` or "dark gray". OLED loves true black; it disappears.
- **Yellow accent** (`UIColor.systemYellow`) for active controls — the iconic Apple Camera convention. Branded apps replace with their accent, but yellow communicates "active manual control".
- **Backdrop blurs**: use `UIVisualEffectView` with `.systemUltraThinMaterialDark` for floating control palettes. On iOS 26+, prefer the new `.glassEffect()` modifier or `expo-glass-effect` style Liquid Glass surfaces — but ONLY if your app's overall design language is Liquid Glass. Mixing styles looks broken.
- **Photo previews**: pure black background. Never a pattern, never a gradient, never a card. Photos against black is iconic for a reason.
- **Chrome palette via OKLCH (ship as Display P3)**: when designing the camera's accent palette (active controls, mode-selected indicators, focus rings, recording dot), pick all colors at the SAME OKLCH `L` value (e.g., `L=0.7`) so they feel like siblings — no color dominates the chrome — then ship them as `Color(.displayP3, ...)` so vivid reds, yellows, and oranges actually render at full chroma on every Apple device. See `the-final-5-percent` §5 for the full workflow. This combination — OKLCH for perceptual consistency, Display P3 for gamut — is what makes Halide and Kino's chrome feel so refined.
- **Histograms use perceptual luminance, not RGB.** If your editing UI shows a histogram, the standard RGB histogram is misleading — pure yellow registers high in R+G but the eye sees it as a single value. Compute luminance via OKLCH `L` (or BT.709 luma at minimum) for an accurate exposure read. Photographers will notice.

### Curiosity-gap sharing — partial reveal for virality

When users share a photo through your app to social platforms (Stories, iMessage), consider a "curiosity-gap" share preview — the Bier viral pattern:

- **Full photo** stays in your app.
- **Shared preview** is partially blurred OR cropped, with a "Tap to see the full photo on [App]" overlay.
- Recipient sees enough to be intrigued, must install to see the rest.

For social camera apps (Locket, Lapse, BeReal-style), this is the difference between a share that converts and a share that gives away your app's value for free.

```swift
@MainActor
func generateTeasePreview(from photo: UIImage) -> UIImage {
    let view = ZStack {
        Image(uiImage: photo)
            .resizable()
            .scaledToFill()
            .blur(radius: 40)               // hide the actual content
        VStack {
            Image(uiImage: photo)            // a small clear teaser strip
                .resizable()
                .scaledToFill()
                .frame(height: 280)
                .clipped()
                .mask(LinearGradient(
                    colors: [.black, .black.opacity(0)],
                    startPoint: .top, endPoint: .bottom
                ))
            Spacer()
            Label("See the full photo on [App]", systemImage: "arrow.up.forward.app.fill")
                .font(.system(.body, design: .rounded, weight: .semibold))
                .foregroundStyle(.white)
                .padding(.bottom, 60)
        }
    }
    .frame(width: 1080, height: 1920)

    let renderer = ImageRenderer(content: view)
    renderer.scale = 3
    return renderer.uiImage ?? photo
}
```

See `the-final-5-percent` shareable image generation section for the full pattern — same `ImageRenderer` foundation, applied to camera-specific tease content.

---

## Novel iOS APIs to consider

This is where you separate the camera app from the *iOS* camera app.

### AVCaptureMultiCamSession (iPhone XS+)
Capture from front + back camera simultaneously. Apps like BeReal use this. Picture-in-picture composition: overlay the front camera in a 130 × 200pt rounded rect at the top-left of the back-camera frame. Use `AVCaptureMultiCamSession` and connect both `AVCaptureDeviceInput`s — preview both layers and record via two parallel `AVCaptureMovieFileOutput`s, then composite with `AVAssetExportSession`.

### LiDAR depth maps (iPhone 12 Pro+)
Use `AVCaptureDepthDataOutput` to grab per-pixel depth. Applications:
- **Real-time bokeh** with controllable aperture (custom Metal shader sampling depth to blur background).
- **3D photos**: parallax effect on the saved photo by storing depth as auxiliary image data (HEIC supports this via `kCGImageAuxiliaryDataTypeDepth`).
- **Object measurement**: tap two points to get the real-world distance.

### Cinematic mode (programmatic — iOS 17.2+)
`AVCaptureMovieFileOutput.isCinematicVideoCaptureEnabled = true` enables shallow-depth video with rack-focus. Show "Cinematic" badge and a focus picker UI: tap a subject to focus, pinch to adjust aperture (f/2.0 to f/16.0).

### ProRAW & Apple ProRes
- ProRAW: `AVCapturePhotoOutput.isAppleProRAWEnabled = true` then set `photoSettings.rawPhotoPixelFormatType` to a Bayer format. Output is a DNG file with full editing latitude.
- ProRes: video pros LOVE this. 4K60 ProRes 422 HQ on iPhone 15 Pro+.

### Spatial photos & spatial video (iPhone 15 Pro+)
`AVCaptureMovieFileOutput.spatialVideoCaptureEnabled = true` (with the appropriate device format) captures stereoscopic video viewable on Apple Vision Pro. This is a meaningful differentiator — most camera apps don't support it. Indicate spatial captures in the library with a small 3D-cube badge.

### Camera Control button (iPhone 16/16 Pro)
`AVCaptureEventInteraction` provides callbacks for camera button events:
- **Half-press**: focus & exposure lock. UI: brief yellow ring pulse on the viewfinder.
- **Full-press**: capture.
- **Light-touch slide**: parameter adjustment (zoom, exposure compensation, depth). Surface a contextual control overlay during the slide.
- **Double light-press**: cycle through controls.

```swift
let interaction = AVCaptureEventInteraction { event in
    switch event.phase {
    case .began: shutterPressed()
    case .ended: shutterReleased()
    @unknown default: break
    }
}
viewController.view.addInteraction(interaction)
```

### VisionKit DataScannerViewController
Native QR/barcode/text scanning with a presentational UI Apple controls.

```swift
import VisionKit

let scanner = DataScannerViewController(
    recognizedDataTypes: [.barcode(), .text(textContentType: .URL)],
    qualityLevel: .balanced,
    recognizesMultipleItems: true,
    isHighFrameRateTrackingEnabled: true,
    isGuidanceEnabled: true,
    isHighlightingEnabled: true
)
try scanner.startScanning()
```

Pair with a custom UI on top: highlight detected items with animated outlines, show a contextual sheet for the most-confident detection.

### Live Text (VNRecognizeTextRequest)
"Select text from any photo" — pair with `ImageAnalysisInteraction`. Bonus: detect phone numbers, addresses, dates in OCR results and offer one-tap actions.

### Vision framework (face, body, hand, animal detection)
- `VNDetectFaceLandmarksRequest`: face boxes + landmarks for smart cropping, beauty effects.
- `VNHumanBodyPoseObservation`: skeletal pose for "fitness selfie" apps or motion analysis.
- `VNRecognizeAnimalsRequest`: cat/dog detection for pet-focused apps (Lapse uses something like this).
- `VNGenerateImageFeaturePrintRequest`: image similarity / visual search — "find more like this" in the library.

### Core ML on-device aesthetics scoring
Train a tiny CoreML model (or use existing Apple sample) that scores image aesthetics. Use it to:
- Auto-pick "best of burst" frames.
- Surface "your best photos this week" features.
- Filter the library by quality automatically.

### CreateML personalized style transfer
Let the user pick 10–20 of their favorite photos and train a CreateML style transfer model on-device. Then offer a "Your Style" filter — uniquely personalized to that user. NOBODY does this. It would be magical.

### ARKit face tracking for filters
For Snapchat-style face filters, `ARFaceTrackingConfiguration` gives you a 1220-vertex face mesh, 52 blendshapes, and gaze direction. Render filters with SceneKit or Metal. Bonus: the TrueDepth camera also gives accurate depth on the face — perfect for "studio lighting" simulation.

### RoomPlan (iPhone Pro / iPad Pro w/ LiDAR)
For interior/architecture photographers: scan a room into a 3D parametric model. Save alongside the photos for documentation.

### App Intents — Siri & Shortcuts
Expose camera actions as App Intents:
- "Take a selfie with the [Vintage] filter" → opens app, switches to front cam, applies filter, captures.
- "Show my Lapse photos from last weekend" → opens library scoped to date range.

```swift
struct CapturePhotoIntent: AppIntent {
    static var title: LocalizedStringResource = "Take a photo"
    static var openAppWhenRun = true

    @Parameter(title: "Filter")
    var filter: FilterEntity?

    func perform() async throws -> some IntentResult {
        await CameraSession.shared.capture(filter: filter)
        return .result()
    }
}
```

### Live Activities + Dynamic Island for long-running exports
When the user exports a 4K timelapse or batch-applies a filter to 200 photos, surface a Live Activity:
- Lock screen: progress bar + "Exporting 47/200".
- Dynamic Island: progress ring with the current thumbnail.
- Tap to deep-link back to the export screen.

### Background URL Session for cloud upload
For apps that auto-backup or sync, use `URLSession` with `URLSessionConfiguration.background(withIdentifier:)`. Uploads continue when the app is suspended.

### TipKit for first-run discovery
Use `TipView` to surface "Tap and hold to lock AE/AF" the first time someone takes 3+ photos in a session. Apple's framework, perfect for camera UX onboarding.

### PHPickerViewController (privacy-first photo picking)
For any "pick a photo from your library" flow, NEVER request full photo library access (`.authorized`). Use `PHPickerViewController` — Apple grants temporary access to just the selected photo without showing a permission prompt.

### Symbol Effects (iOS 17+)
For toolbar icons (flash, flip camera, settings), use `.symbolEffect(.bounce, value: trigger)` on `Image(systemName:)` — adds delightful motion without writing animation code.

```swift
Image(systemName: "bolt.fill")
    .symbolEffect(.bounce, value: flashTrigger)
    .symbolRenderingMode(.hierarchical)
```

### Metal shaders for filters
Don't ship filters as `CIFilter` chains in 2026. Write custom Metal compute kernels for filters — 10× the perf, and lets you ship effects that don't exist in Core Image (custom LUTs with proper gamma, true grain, etc.). Use `MTKView` for the preview.

---

## Anti-patterns to avoid

1. **Showing a launch screen** between tap and viewfinder. The camera should be live in < 250ms. If you can't make that, you have an architecture problem.
2. **Putting controls behind a hamburger menu.** Cameras are about hierarchy — the 3 most-used controls (shutter, flip, flash) should be permanent. Everything else can hide.
3. **A shutter button that isn't a circle.** This is the most established visual metaphor in mobile UI. Don't innovate here.
4. **Confirming "Photo saved!" with a toast.** The thumbnail flying to the corner IS the confirmation. The toast is noise.
5. **Tying haptic intensity to gesture velocity.** Camera haptics should be precise, not expressive. Pick the right impact style and use it consistently.
6. **Using gradients on UI elements that overlay the viewfinder.** They pull attention from the photo. Flat translucent black or true black only.
7. **Animations longer than 400ms for any in-app transition.** You're a tool. People want to take photos, not watch your transitions.
8. **Forgetting Reduce Motion**. Camera apps are heavily used by people with vestibular sensitivities (lots of motion in the viewfinder). Respect the setting.
9. **Not implementing volume-button shutter.** Casual users don't know about it; enthusiasts will not use your app without it.
10. **Wasting the bottom 100pt of the viewfinder for chrome on edge-to-edge devices.** Yes, the home indicator is there. But you can render UI BEHIND the indicator with a subtle backdrop blur instead of cropping the preview.

---

## Permissions UX

Camera and photo library permission prompts are make-or-break.

**Camera permission**:
- Pre-prompt: show a beautiful explanation screen BEFORE calling `AVCaptureDevice.requestAccess(for: .video)`. Title: "Let [App] use your camera". Body: 2-3 lines on what you'll do with it (e.g., "We'll process all photos on your device. Nothing is uploaded.").
- If denied: redirect to Settings with a graceful "We need camera access to continue" screen. NEVER block the entire app on denial — show what's possible without (e.g., the library).
- Re-prompt: you only get ONE shot at the system prompt. Make it count.

**Photo library permission**:
- ALWAYS prefer `.limited` access via `PHPicker` or by requesting `.addOnly` (write-only) where possible.
- If you must request full library access, explain why explicitly: "To show your library inside the app, we need access to your photos. We don't read EXIF or upload anything."
- Respect "Selected Photos" mode — your app must work with a partial library.

---

## Performance bar

Anything below these numbers is unacceptable for a camera app shipping in 2026:

| Metric | Bar |
| --- | --- |
| Cold-start to live viewfinder | ≤ 500ms |
| Warm-start (app was backgrounded < 5s ago) | ≤ 120ms |
| Shutter press → photo capture event | ≤ 50ms |
| Capture event → thumbnail visible | ≤ 200ms |
| Filter preview FPS | 60fps (or 120fps on ProMotion) |
| Library scroll | 60fps (120fps on ProMotion) — never drop frames |
| Image edit save → library updated | ≤ 600ms for an iPhone-resolution image |
| Memory ceiling during burst capture | < 350MB |

Profile with Instruments: Time Profiler, Allocations, and especially **Metal System Trace** for filter performance.

---

## Implementation checklist for a new camera app

Use this when starting from zero:

- [ ] **Session**: `AVCaptureSession` configured on a background queue. `.startRunning()` called off main thread.
- [ ] **Preview layer**: `AVCaptureVideoPreviewLayer` with `.videoGravity = .resizeAspectFill`.
- [ ] **Photo output**: `AVCapturePhotoOutput` configured for max-resolution HEIC + ProRAW if device supports.
- [ ] **Live preview rendering**: `AVCaptureVideoDataOutput` → Metal shader chain for filters (don't use `AVCaptureVideoPreviewLayer` if you need real-time filters).
- [ ] **Mode switcher**: horizontal paging scroll view with haptic + spring snap.
- [ ] **Shutter**: 76pt outer ring, 60pt inner fill, scale-on-press, haptic + flash on capture.
- [ ] **Focus/exposure tap**: 80pt yellow square with pulse animation, EV slider, AE/AF lock.
- [ ] **Pinch-to-zoom**: log-mapped to zoom factor, with on-screen indicator.
- [ ] **Volume button capture**: `AVCaptureEventInteraction` (iOS 17.2+).
- [ ] **Camera Control button** (iPhone 16+): half-press focus, full-press capture, slide for parameter.
- [ ] **Live Photos**: enabled by default with toggle in chrome.
- [ ] **Grid lines**: thirds + level + horizon detection.
- [ ] **Flash control**: off/on/auto with `.symbolEffect(.bounce)` on toggle.
- [ ] **Front camera flip**: animated 3D flip transition or simple crossfade — pick one and commit.
- [ ] **Settings sheet**: half-modal (`.presentationDetents([.medium])`) with the rest of the controls.
- [ ] **Library access**: `PHPicker` for selection, `.addOnly` permission for saving.
- [ ] **Thumbnail flight**: hero animation from viewfinder center to gallery button.
- [ ] **Background save**: photo writes to PhotoKit via `PHAssetCreationRequest` on a background queue.
- [ ] **Haptics**: prepared on every gesture begin, fired with appropriate generators.
- [ ] **Reduce Motion**: alternative non-spring transitions when enabled.
- [ ] **Reduce Transparency**: opaque chrome backgrounds when enabled.
- [ ] **Increase Contrast**: bolder borders and higher-contrast text when enabled.
- [ ] **Spatial photo/video** (iPhone 15 Pro+): captured by default for users on Vision Pro households.
- [ ] **Permission pre-prompt**: explainer screen before system prompt.
- [ ] **First-run TipKit**: surface manual controls after 3 captures.
- [ ] **App Intents**: at least "Take a photo" and "Open library" exposed to Siri.

---

## Final principles

1. **The viewfinder is the product.** Everything else is in service of it.
2. **Latency is a feature.** Saving 100ms on launch is worth more than any filter.
3. **Haptics confirm; visuals communicate.** Don't use one to do the other's job.
4. **Respect the photographer.** Show them the real exposure histogram. Don't auto-enhance their RAWs.
5. **A great camera app is invisible.** When users put it away, they should remember the photo, not your UI.

The benchmark: someone uses your app for a week, takes a photo they're proud of, and tells a friend — but can't quite remember which app it was, just that "the camera felt amazing." That's the goal.
