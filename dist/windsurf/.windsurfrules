# iOS Design Engineering Skills

This document encodes four detailed design-engineering skills for building
best-in-class native iOS/SwiftUI apps. When working on Swift/SwiftUI code,
consult the relevant section based on what you're building.

## Index

- **iOS Camera & Photos** — see `## iOS Camera & Photos` below
- **iOS Chat & Messaging** — see `## iOS Chat & Messaging` below
- **iOS Interaction Primitives (Widgets, Live Activities, Haptics)** — see `## iOS Interaction Primitives (Widgets, Live Activities, Haptics)` below
- **The Final 5% — iOS Polish** — see `## The Final 5% — iOS Polish` below

---

## iOS Camera & Photos

_When to use this section: Design and build best-in-class native iOS camera, photo-capture, and photo-editing apps with the polish of Halide, Kino, Lapse, VSCO, and Apple Photos. Use this skill whenever the user is building, reviewing, or refining a SwiftUI/UIKit app that involves the camera, photo library, video capture, image editing, filters, scanning, AR effects, AI photo features, or anything backed by AVFoundation, PhotoKit, Vision, VisionKit, Core Image, ImageCaptureCore, ARKit, RoomPlan, or LiDAR. Triggers on: camera, viewfinder, shutter button, capture, AVCaptureSession, AVCapturePhotoOutput, AVCaptureMovieFileOutput, PHPicker, PhotoKit, photo library, photo gallery, photo grid, photo edit, photo filter, photo crop, photo adjustment, sliders, presets, LUT, Cinematic mode, Portrait mode, ProRAW, Apple ProRes, Live Photos, HDR, Smart HDR, depth, LiDAR, subject lifting, VisionKit, Live Text, DataScannerViewController, document scanner, QR scanner, barcode, scanner, magic eraser, object removal, sky replacement, AI photo, on-device ML, Core ML, Vision framework, ARKit face tracking, Snapchat-style filters, AR effects, lens, beauty filter, focus, exposure, white balance, ISO, shutter speed, manual camera controls, Camera Control button, volume button shutter, spatial photo, spatial video, Apple Vision Pro._

# iOS Camera & Photos — Design Engineering Skill

A taste guide for building camera and photo apps that feel like they were made by people who actually shoot photos. Every value in this file is opinionated and specific — pulled from studying flows on Mobbin and shipping native iOS apps.

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
- **Chrome palette via OKLCH**: when designing the camera's accent palette (active controls, mode-selected indicators, focus rings, recording dot), pick all colors at the SAME OKLCH `L` value (e.g., `L=0.7`) so they feel like siblings — no color dominates the chrome. See `the-final-5-percent` §5 for the full workflow. This is what makes Halide and Kino's chrome feel so refined: every active indicator has the same perceived brightness as every other.
- **Histograms use perceptual luminance, not RGB.** If your editing UI shows a histogram, the standard RGB histogram is misleading — pure yellow registers high in R+G but the eye sees it as a single value. Compute luminance via OKLCH `L` (or BT.709 luma at minimum) for an accurate exposure read. Photographers will notice.

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


---

## iOS Chat & Messaging

_When to use this section: Design and build best-in-class native iOS chat, messaging, and group chat apps with the polish of iMessage, Telegram, WhatsApp, Snapchat, Instagram DMs, and Discord. Use this skill whenever the user is building, reviewing, or refining a SwiftUI/UIKit app that involves direct messages, group chats, threads, voice messages, video calls, reactions, typing indicators, presence, read receipts, ephemeral messages, end-to-end encryption, push notifications, or anything backed by APNs, PushKit, CallKit, CryptoKit, NotificationServiceExtension, or Live Activities. Triggers on: chat, messaging, message bubble, group chat, DM, direct message, conversation, composer, message input, reactions, tapback, emoji reaction, reply, thread, threaded reply, typing indicator, presence, online status, last seen, read receipt, double check, blue check, voice message, audio message, push-to-talk, voice note, waveform, end-to-end encryption, E2EE, Signal protocol, ephemeral, disappearing message, view once, self-destruct, sticker, GIF, animated emoji, Genmoji, iMessage app, message effect, confetti, balloons, Live Activity, Dynamic Island, push notification, NSE, notification service extension, CallKit, PushKit, video call, audio call, FaceTime, Communication Notification, Shared with You, SharePlay, App Clip, App Intent, Siri Send Message, CryptoKit._

# iOS Chat & Messaging — Design Engineering Skill

A taste guide for building messaging apps that feel like they belong on iOS. Every value below is opinionated and specific — pulled from studying flows on Mobbin and shipping native chat apps.

## Philosophy

> A chat app is a feeling of being heard, fast.

Three things separate amazing chat from passable chat:
1. **The composer is the only thing that matters.** Everything else is supporting cast. Time-to-typing must be < 200ms from launch. Send must be instant — show the bubble before the network responds. If you can't get this right, nothing else matters.
2. **Bubbles are a writing system.** Spacing, grouping, tail placement, and timestamp rhythm communicate WHO said WHAT WHEN faster than reading the text itself. Get the visual language right and people skim conversations 3× faster.
3. **Latency is the product.** A message that sends in 80ms but arrives in 2000ms feels slower than one that sends in 800ms and arrives in 900ms. Optimistic UI is not optional.

The pixel-pushers' rules:
- **Bubbles, not cards.** A card has shadows and borders. A bubble has a tail. Chat is conversation, not content.
- **The composer is permanent.** It sits at the bottom always, even during search, even during the empty state. Never push the composer above the fold.
- **Read receipts are intimate.** Default them OFF for new users. Telegram and Signal got this right.
- **Don't infantilize.** No "Looks like there are no messages here yet!" cute illustrations in a serious chat app. Empty states should be quiet.

## Reference apps to study

When in doubt, copy. These are the apps you should be benchmarking against, with the specific flows worth lifting:

| App | What to learn from it | Mobbin flow |
| --- | --- | --- |
| **Apple Messages (iMessage)** | The gold standard for native feel — bubble tails, tapbacks, message effects, Genmoji, inline App Clips, Communication Notifications. Everything compiles against this. | (Use the system; observe it on your own device) |
| **Telegram** | The most feature-dense chat app ever built. Auto-delete timers, custom themes per chat, last-seen privacy ladders, reactions with custom emoji, animated stickers (TGS/Lottie), folder-based chat lists | [Last Seen settings](https://mobbin.com/flows/3bc6e47e-6e9d-4f11-bcd0-0939ad3db4f9), [Reacting to a message](https://mobbin.com/flows/65a949d7-6d85-4ba3-93eb-62bfcf0ddc17) |
| **WhatsApp** | Voice messages done right, read receipts (gray → blue double check), reply-with-swipe-right, message info screen, end-to-end encryption banner, edit window (15min) | [Message info](https://mobbin.com/flows/91134f85-10a8-48e5-96cf-84f3f67830eb) |
| **Snapchat** | Ephemeral messages, "save in chat", time-limit picker, screenshot detection notifications, voice notes with transcription | [Setting time limit](https://mobbin.com/flows/4fa7c0d5-b4dd-461a-a732-61fa1b0e848d), [Recording audio](https://mobbin.com/flows/54b4693a-a82e-4346-afc5-8a0036a44952), [Deleting a message](https://mobbin.com/flows/68ff8963-fcd2-403e-88fb-05554bfb8aa5) |
| **Instagram DMs** | Per-chat themes, reaction picker w/ "tap and hold to super-react", reply-with-context, Notes (lightweight broadcast) | [Reacting to a message](https://mobbin.com/flows/bbd7c647-0100-47d8-b759-4a5b4c4d7de0), [Creating group chat](https://mobbin.com/flows/cdb301fd-273d-47cc-a760-82ed02883f71) |
| **LINE** | Sticker-first design language, contextual long-press menu (12 actions), stamp reactions, expressive avatars | [Reacting to a message](https://mobbin.com/flows/75fb375d-fd08-4a05-b652-c0f005b27681) |
| **Discord** | Presence states (Online/Idle/DND/Invisible), server/channel hierarchy, voice channels w/ live activity | [Changing status](https://mobbin.com/flows/7d691cf7-9ec9-483a-9d97-f3b29fd84633) |
| **WeChat / Taobao** | Push-to-talk voice (hold mic button), in-bubble voice-to-text transcribe, lift-to-ear playback | [WeChat voice](https://mobbin.com/flows/b043b433-ef7d-4eff-9393-8ae5958d48fc), [Taobao voice](https://mobbin.com/flows/9bc4139a-bcae-4070-bdb8-2f3423f40c6a) |
| **Luma / Beside** | Group chat creation with custom emoji avatar + theme color, clean conversation list, suggested replies | [Luma create group](https://mobbin.com/flows/45c43eee-a684-4730-a1c3-7f26eba77d38), [Beside create group](https://mobbin.com/flows/769561b5-e079-489b-a124-d99355d970d4) |
| **Microsoft Teams** | Embedded calls in chat, threaded replies, suggested message starters | [Creating a chat](https://mobbin.com/flows/beb5079a-8928-473a-9228-42d3106635c3) |
| **Pi (Inflection AI) / Replika** | AI chat with voice input, typing indicator that animates, transcription mid-stream | [Pi reactions](https://mobbin.com/flows/99931f05-5968-4759-b40e-0e891e0492e9), [Replika voice](https://mobbin.com/flows/e0d853a4-037e-415a-b18f-076b2972aa51) |
| **Locket** | Broadcast-style "message everyone": photo capture is the message; no library, no scroll | [Locket camera](https://mobbin.com/flows/a16e33e2-501a-4c26-ac00-ab960e345040) |
| **PlayStation App** | Reaction picker positioning, "PLEASE WAIT" giant stickers, game-context chat | [Chat detail](https://mobbin.com/flows/acbebeb5-566a-4985-99ec-0b29be8a3e23) |
| **Skype** | Status broadcast ("Share what you're up to"), DND with explanatory modal | [Availability status](https://mobbin.com/flows/2daa6dba-5f7b-4c14-a0ee-c3599e1b1d4d) |

---

## Hero interactions — the moments that matter

### 1. The message bubble

The bubble is the writing system. Get it perfect:

**Geometry:**
- **Corner radius**: 18pt (continuous corner / squircle, NOT system circular). Use `RoundedRectangle(cornerRadius: 18, style: .continuous)` in SwiftUI or `.layer.cornerCurve = .continuous` in UIKit.
- **Max width**: 75% of screen width (`UIScreen.main.bounds.width * 0.75`). Wider than that, the rag-right edge becomes ugly and reading speed drops.
- **Internal padding**: 12pt horizontal, 8pt vertical (single-line bubbles). For multi-line, increase vertical to 10pt.
- **Bubble-to-bubble spacing within a group**: 2pt.
- **Bubble-to-bubble spacing across senders**: 14pt.
- **Bubble-to-bubble spacing across time gaps**: 24pt + an inline timestamp pill.

**Colors:**
- **Sent (self) bubble**: `Color.accentColor` (iMessage blue) at 100%, white text. For app brand variations, use the brand accent but ALWAYS check contrast (WCAG AA against the chosen text color).
- **Received bubble**: `Color(.tertiarySystemGroupedBackground)` for light mode, `Color(.systemGray5)` for dark mode. Text color: `.label` (auto-adapts).
- **Failed-to-send bubble**: same shape as sent, but with a 1pt red border and a red exclamation icon to the right.
- **Pending/queued bubble**: 60% opacity of the sent bubble. Settles to 100% on delivery confirmation.

**Bubble grouping (THE critical detail):**

Consecutive messages from the same sender within 60 seconds form a "burst". A burst has:
- The FIRST bubble: full radius on the outside corner (top-right for sent, top-left for received), 4pt small radius on the inside (touching) corner.
- The MIDDLE bubbles: 4pt small radius on the inside corners, full 18pt on the outside.
- The LAST bubble: full radius on the outside corners (top-right + bottom-right for sent), with the tail extending from the corner.

```swift
enum BubblePosition {
    case single, first, middle, last
}

func cornerRadii(for position: BubblePosition, isSent: Bool) -> RectangleCornerRadii {
    let small: CGFloat = 4
    let large: CGFloat = 18
    let outer = isSent ? "right" : "left"
    switch position {
    case .single: return .init(topLeading: large, bottomLeading: large, bottomTrailing: large, topTrailing: large)
    case .first:  return isSent
        ? .init(topLeading: large, bottomLeading: large, bottomTrailing: small, topTrailing: large)
        : .init(topLeading: large, bottomLeading: small, bottomTrailing: large, topTrailing: large)
    case .middle: return isSent
        ? .init(topLeading: large, bottomLeading: large, bottomTrailing: small, topTrailing: small)
        : .init(topLeading: small, bottomLeading: small, bottomTrailing: large, topTrailing: large)
    case .last:   return isSent
        ? .init(topLeading: large, bottomLeading: large, bottomTrailing: large, topTrailing: small)
        : .init(topLeading: small, bottomLeading: large, bottomTrailing: large, topTrailing: large)
    }
}
```

**The tail** (iMessage convention):
- Only render the tail on the LAST bubble of a burst.
- Tail is a small ~6 × 8pt curved triangle that emerges from the outside-bottom corner.
- Implement with a custom `Path` (a quadratic Bezier sweeping from the bubble's edge outward and back).
- For sent: tail on bottom-right, pointing right.
- For received: tail on bottom-left, pointing left.

**Avatars** (received messages only):
- Show only on the LAST bubble of a received burst (matches the tail).
- 28pt circle, 8pt to the left of the bubble.
- 1pt subtle border in `Color(.separator)` to give edge against light backgrounds.

**Typography inside bubbles:**
- Body text: SF Pro, regular, 17pt, line height 22pt.
- For shorter messages (≤ 3 emoji), AUTO-SCALE the emoji to 48pt and remove the bubble. iMessage does this. It makes single-emoji messages feel alive.

### 2. The composer

The composer is the most-used surface in your entire app. Treat it that way.

**Geometry:**
- **Height (collapsed)**: 36pt for the input pill + 8pt vertical safe-area padding above + 8pt below.
- **Pill background**: `Color(.tertiarySystemBackground)` with `cornerRadius: 18, style: .continuous` (matching bubble radius).
- **Pill horizontal padding**: 12pt left, 12pt right (text content area).
- **Pill grows** as user types up to 5 lines. After 5 lines, scroll internally.
- **+ button (attachment)**: 28pt circle to the LEFT of the pill, 8pt spacing. Subtle gray fill.
- **Mic / Send button**: 28pt circle to the RIGHT of the pill, 8pt spacing.

**Mic ↔ Send swap** (THE detail):
- When the text field is empty: mic icon appears on the right.
- When user types ANY character: mic morphs into send arrow with `scale 0 → 1` + `opacity 0 → 1` (180ms `.spring(response: 0.32, dampingFraction: 0.7)`). Mic crossfades out simultaneously.
- When user deletes back to empty: reverse.
- Haptic `.selectionChanged` on each swap.

**Keyboard handling:**
- The composer MUST stick to the top of the keyboard. Use `keyboardLayoutGuide` (UIKit) or `.ignoresSafeArea(.keyboard, edges: .bottom)` with explicit padding (SwiftUI).
- When keyboard appears, the bubble list scrolls to the bottom with NO animation (or 80ms `.linear`). The keyboard's animation curve (`UIView.AnimationCurve` from the notification) is what you should match.
- **Critical**: don't let the bubble list jump. Compute the offset and apply it within `UIView.animate(withDuration: keyboardAnimationDuration, delay: 0, options: .curveSetting)` — this matches the keyboard's curve perfectly.

**Return key polish (`.submitLabel`):**
- Set `.submitLabel(.send)` on the text field so the keyboard's return key shows "send" — not a generic return arrow. Available labels: `.done`, `.go`, `.next`, `.return`, `.search`, `.send`, `.join`, `.route`, `.continue`. Match the verb to the action.
- Wire `.onSubmit { send() }` so the return key actually fires the send. iOS keyboards expect this.
- For multi-line composers where Return should insert a newline, don't override — let the system handle it. Pair with a dedicated send button.

```swift
TextField("Message", text: $draft, axis: .vertical)
    .lineLimit(1...5)
    .submitLabel(.send)
    .onSubmit { send() }
```

**Send animation:**
1. User taps send. IMMEDIATELY (within 16ms):
2. The bubble appears at the composer's text position with full opacity but at 70% scale.
3. The text field clears.
4. The bubble flies up to its slot in the list with `matchedGeometryEffect` (SwiftUI) or `UIView.transitionWithView` (UIKit), scaling 0.7 → 1.0 + slight overshoot to 1.04 → settle.
5. Spring: `.spring(response: 0.42, dampingFraction: 0.78)`.
6. Haptic on send: `UIImpactFeedbackGenerator(.light).impactOccurred()` at the moment of release.
7. If the send eventually fails: bubble subtly desaturates (60% opacity) and a red `!` appears beside it. Tap to retry. Haptic `.error`.

**The signature detail: the loading indicator travels.** If sending is slow enough to need a progress hint, DON'T show it at the send button — show it INSIDE the optimistically-rendered bubble in the conversation. The eye follows one focal point: the bubble. A 12pt circular `ProgressView` aligned to the bubble's trailing edge does the job. When delivery confirms, the indicator dissolves and the read receipt fades in beside it. This is the [Family Values pattern](https://benji.org/family-values) — loading states travel to their destination.

### 3. Reactions / tapbacks

The long-press → bubble lifts → reaction picker appears flow.

**Long-press detection:**
- 0.45 second long-press triggers the menu (slightly faster than iOS default of 0.5).
- During the press, the bubble subtly scales to 1.02 (signaling "you're activating me").
- At the threshold: bubble lifts to 1.04, background blurs (`UIBlurEffect(style: .systemUltraThinMaterialDark)` or `.glassEffect()` on iOS 26+).
- Haptic on threshold cross: `UIImpactFeedbackGenerator(.medium).impactOccurred()`.

**Reaction picker:**
- A horizontal pill containing 6 quick emojis + a "+" for the full picker. Positioned ABOVE the bubble (or below if the bubble is at the top of the screen).
- Animation:
  - Pill scales from 0 (origin at the bubble's nearest corner) to 1.0 with `.spring(response: 0.36, dampingFraction: 0.72)`.
  - Emoji icons inside the pill stagger their entrance: each 0.04s after the previous, scale 0 → 1.0 with overshoot.
- Tapping an emoji:
  - Haptic `.medium`.
  - The emoji animates from the picker to its final position on the bubble (corner overlap), shrinking from 38pt to 16pt as it lands.
  - The picker dismisses with `scale 1 → 0` (180ms `.easeIn`).
- Tapping outside dismisses with no haptic.

**Reaction badges on bubbles:**
- Position: overlapping the corner of the bubble (top-right for sent, top-left for received), 8pt × 8pt overlap into the bubble.
- Geometry: pill shape, 22pt tall, dynamic width. White background (system grouped background), 0.5pt subtle border.
- Multiple reactions: each emoji + count, e.g., "❤️ 3 😂 1".
- Tap a reaction to add your own (toggles). Long-press for the "who reacted" detail sheet.

**Tapback context menu** (additional actions besides reaction):
- Same long-press trigger. Below the reaction pill, a context menu appears with: Reply, Copy, Forward, Pin, Translate, Edit (if your own message, within 15min), Info, Delete.
- Style: `UIMenu` (UIKit) or `.contextMenu` (SwiftUI), but custom-positioned to appear right under the reaction pill. iMessage's choreography is the reference.

### 4. Reply with swipe (WhatsApp / iMessage)

The "swipe-right on a bubble to reply" gesture is essential. Implementation:

```swift
.gesture(
    DragGesture(minimumDistance: 16)
        .onChanged { value in
            let dx = max(0, value.translation.width)
            offset = min(dx, 80) // cap at 80pt
            // Show a reply arrow icon fading in as dx grows
            replyIndicatorOpacity = min(1.0, dx / 60)
            // Haptic when crossing threshold
            if dx > 60 && !hasFiredHaptic {
                UIImpactFeedbackGenerator(style: .soft).impactOccurred()
                hasFiredHaptic = true
            }
        }
        .onEnded { value in
            if value.translation.width > 60 {
                onReply()
            }
            withAnimation(.spring(response: 0.32, dampingFraction: 0.78)) {
                offset = 0; replyIndicatorOpacity = 0
            }
            hasFiredHaptic = false
        }
)
```

**Reply chip in composer:**
- Once user has tapped reply (or completed the swipe), a chip appears ABOVE the input pill:
  - Vertical accent-color bar (3pt × full height) on the left.
  - Original sender's name (semibold, 13pt, accent color).
  - Truncated original message text (regular, 13pt, secondary label, single line, with `...` truncation).
  - "×" close button on the right.
- The chip animates IN with `.spring(response: 0.32, dampingFraction: 0.85)` + slide-up + opacity.
- When the reply is sent, the original message reference is preserved on the new bubble (inline at the top of the bubble), and TAPPING that inline reference scrolls to the original with a yellow flash highlight (0.6s, `.easeOut`).

### 5. Voice messages

This is where second-rate apps fail. Get the WhatsApp pattern right:

**Recording:**
- The mic icon (right of composer) is the trigger. **Hold to record**, release to send. NOT tap-toggle.
- On press-down:
  - Haptic `.medium`.
  - The composer transforms: the text pill is replaced with a recording indicator (red dot pulsing + timer "0:03"), and a "← slide to cancel" hint appears.
  - The mic icon grows to ~52pt and slides slightly left.
  - A live waveform builds along the bottom of the screen.
- During hold:
  - **Slide LEFT past 80pt**: cancel. Haptic `.warning`, recording discarded, UI restores.
  - **Slide UP past 60pt**: lock. The mic icon snaps into a "lock" position; user can release and continue recording hands-free. Haptic `.success`.
  - **Release in place**: send. Haptic `.light`.

**Live waveform:**
- Use `AVAudioRecorder` with metering enabled. Poll `averagePower(forChannel: 0)` every 50ms.
- Render 60–80 vertical bars, mirrored vertically (symmetric around the center). Bar width 2pt, gap 2pt.
- Each new sample shifts the bars left and appends a new bar at the right.
- Bar colors: accent color for "speech" (power > threshold), gray for "silence".

**Playback bubble:**
- 240pt × 56pt rounded bubble.
- Inside: 32pt play/pause button on the left (system play icon), waveform in the middle, duration text on the right.
- The waveform is a STATIC visualization of the recording (pre-computed from the audio samples, downsampled to fit the bubble width).
- Scrubbing: drag finger across the waveform to scrub through playback. Haptic `.soft` every 0.5s of audio crossed.
- Tap-to-play: `UIImpactFeedbackGenerator(.light).impactOccurred()` on tap.
- **Speed control**: small "1×" pill bottom-right; tap to cycle 1× → 1.5× → 2× → 1×.

**Lift-to-ear playback** (WhatsApp pattern):
- When a voice message is playing and the user lifts the phone to their ear, switch audio output from speaker to earpiece using `AVAudioSession`.
- Detect proximity with `UIDevice.current.isProximityMonitoringEnabled = true` and observe `proximityStateDidChangeNotification`.
- This is incredibly delightful when it works.

**Transcription** (on-device, iOS 13+):
- After recording, run `SFSpeechRecognizer` on-device (`requiresOnDeviceRecognition = true`).
- Show a small "Aa" button on the voice bubble; tap to reveal the transcription below the waveform.
- Cache transcriptions; don't re-run.
- For new messages: kick off transcription immediately when received so the "Aa" button reveals instantly.

### 6. Typing indicators

The three-dot animation is iconic but you have to do it right.

**Visual:**
- Three dots, 7pt diameter each, 4pt gap between them.
- Inside a mini bubble: same color/shape as a received bubble, smaller (height 22pt), positioned at the receiver's NEXT bubble location.
- Dots animate: each rises by 3pt, with staggered timing. Dot 1 starts at t=0, dot 2 at t=0.15s, dot 3 at t=0.3s. Each cycle is 0.9s (rise → fall).
- Easing: `.easeInOut` for the rise/fall.

**Behavior:**
- Show after 0.5s of detected typing (don't fire on every keystroke).
- Hide after 2.5s of no typing (or immediately when a message is received).
- Animate IN with `.spring(response: 0.32, dampingFraction: 0.78)` (scale 0 → 1.0 + opacity).
- Animate OUT with `scale 1 → 0` (180ms `.easeIn`).
- Persistence: typing indicators should survive a brief network drop (cache the last "typing" event for 4s).

```swift
struct TypingDots: View {
    @State private var animating = false
    var body: some View {
        HStack(spacing: 4) {
            ForEach(0..<3) { i in
                Circle()
                    .frame(width: 7, height: 7)
                    .offset(y: animating ? -3 : 0)
                    .animation(
                        .easeInOut(duration: 0.45)
                        .repeatForever(autoreverses: true)
                        .delay(Double(i) * 0.15),
                        value: animating
                    )
            }
        }
        .onAppear { animating = true }
    }
}
```

### 7. Read receipts

This is sociologically loaded UI — design it carefully.

**Visual options** (pick one and commit):
1. **iMessage**: small "Delivered" or "Read 2:34 PM" beneath the LAST sent bubble.
2. **WhatsApp**: single check (sent) → double gray check (delivered) → double blue check (read), positioned inside the bubble at the bottom-right.
3. **Telegram**: single check (sent), double check (delivered/read combined).
4. **Signal**: outlined check (sent), filled check (delivered), double check (read).

**Animation**:
- Each state transition animates the check icon with a tiny `.symbolEffect(.bounce)` (iOS 17+) or a custom 200ms scale-up-and-back.
- Haptic on "read" transition (only for sent messages): `UIImpactFeedbackGenerator(.soft).impactOccurred()` ONCE per conversation per session — multiple reads should NOT haptic-spam.

**Privacy settings** (Telegram's gold standard):
- Default: read receipts OFF for new users (controversial but more humane).
- Three tiers: Everybody, My Contacts, Nobody.
- "Hide Read Time" toggle (subtle: read receipts work but timestamps are hidden).
- Exception list: "Always share with these people".

### 8. Presence / Online status

**Online indicator:**
- 8pt green dot, bottom-right corner of avatar, with 2pt white border.
- Inside chat header: "Online" in 13pt regular, secondary label color.

**Last-seen text:**
- "Last seen at 2:34 PM" (today)
- "Last seen yesterday at 9:12 PM"
- "Last seen recently" (vague, Telegram pattern for partial-privacy users)
- "Last seen within a week" (extremely vague)
- "Last seen a long time ago" (the polite "they ghosted")

**Self-disclosed status** (Discord pattern):
- Online (green)
- Idle (yellow, half-moon icon)
- Do Not Disturb (red, no-entry icon)
- Invisible (gray)
- Custom Status (any emoji + text, expiring after 1h / 4h / today / never)

**Active now grouping**: in the chat list, surface a horizontal scroll row of avatars with green dots showing "Active Now". Tap to start a chat.

### 9. Message effects (iMessage-inspired)

Visual effects on send: confetti, fireworks, slam, gentle, invisible ink, etc. Optional but DELIGHTFUL.

**How to implement**:
- Long-press the send button (instead of tapping) to open an effects picker.
- The picker shows: Slam, Loud, Gentle, Invisible Ink, plus full-screen effects (Confetti, Balloons, Fireworks, Lasers, Heart, Spotlight).
- After pick, tap the send arrow to actually send.
- Use `CAEmitterLayer` for particle effects (confetti, fireworks). For more sophisticated effects (lasers, spotlight), use `SCNView` or a custom Metal shader.
- **Reduce Motion**: respect `UIAccessibility.isReduceMotionEnabled` — when true, skip the particle effects but keep the bubble itself (e.g., "Slam" sends as a normal bubble).

**Performance**: limit emitter cells to ~120 particles. Cap effect duration at 3.5s. Always have an "skip" tap target.

### 10. Stickers, GIFs, Genmoji

**Sticker drawer**:
- Surfaced above the keyboard (replacing it) when user taps a sticker icon.
- Top: tab bar with recent stickers, then packs the user owns.
- Each sticker: 88pt × 88pt cell, 8pt gap.
- Tap to send (no preview confirm — fast).
- Long-press to peel the sticker (iOS 17+ peel effect) and drag it onto another part of the conversation (annotation pattern).

**Genmoji** (iOS 18.2+, on-device on Apple Intelligence devices):
- In the keyboard, surface a "Create Genmoji" button.
- User types a prompt; on-device model generates 4 candidate emoji.
- User picks; the Genmoji is sent as a custom sticker.
- Recipients without Apple Intelligence see a PNG fallback.

**GIF picker** (Giphy or Tenor):
- Tab in the sticker drawer or a dedicated icon.
- Search field at top; trending row below.
- Each GIF: tap to send, long-press for preview at full size.

### Trays adopt the environment

When a sticker picker, GIF browser, emoji panel, or any modal is presented from a themed chat (dark theme, custom wallpaper, brand-tinted), it should INHERIT that environment's color scheme — not snap to the system default. A sticker drawer over a dark chat should be dark. A confirmation over a Telegram custom-themed chat should pick up the theme. The visual environment follows the user across modal layers; sudden theme switches are spatially disorienting.

```swift
.sheet(isPresented: $showStickers) {
    StickerPickerView()
        .preferredColorScheme(chatTheme.colorScheme)
        .tint(chatTheme.accent)
        .presentationBackground(chatTheme.surfaceColor)
}
```

This is the design-with-taste "trays adapt to context" rule applied natively.

### 11. Group chat creation

The 3-step flow (Luma / Beside / Instagram pattern):

**Step 1 — Pick people:**
- Top: search field with auto-suggest.
- Below: list of contacts, with a "Suggested" section at the top (frequency-based + recent).
- Selection: tap to add. Selected people appear as chips at the top of the search field (pill, 24pt tall, with avatar + name + × to remove).
- Limit and counter: "3 selected" tracker visible.

**Step 2 — Customize:**
- Group emoji avatar (huge, ~80pt, in a circle): tap to pick from emoji or generate a Genmoji.
- Theme color picker: 6–8 horizontal swatches (Apple style: red, orange, yellow, green, mint, teal, blue, indigo, purple, pink, brown).
- Group name field (optional — default to comma-list of members).
- Description (optional).

**Step 3 — Create:**
- "Create Group Chat" button — full-width pill, 56pt tall, accent color, semibold 17pt text.
- Haptic `.success` on creation.
- Animate the transition to the new chat with a smooth push from the right (standard navigation animation).

### 12. Ephemeral / disappearing messages

**Auto-delete timer** (Telegram pattern):
- Toggle in chat settings, OR a chat-wide setting "Auto-Delete Messages" with options: 24 hours, 7 days, 31 days, off.
- Once set, all messages in the chat get a small clock icon next to the timestamp.
- After the duration, messages fade out with `opacity 1 → 0` over 600ms and are deleted both locally and remotely.

**View-once messages** (WhatsApp / Snapchat):
- Toggle a "view once" icon in the composer before sending an image.
- Recipient sees the message as a blurred placeholder; tap to view, opens full-screen.
- Once viewed, the message turns into "Opened" placeholder forever.
- Snapchat allows a 1–10 second view window (or infinity); WhatsApp allows ONE view, period.

**Screenshot detection** (Snapchat pattern):
- Observe `UIApplication.userDidTakeScreenshotNotification`.
- When detected during a view-once or ephemeral message, send a system message to the other party: "📸 [User] took a screenshot".
- Bonus: also detect screen recording with `UIScreen.main.isCaptured` (KVO).

### 13. End-to-end encryption indicators

**Banner**:
- At the start of any new conversation, a centered system message: "🔒 Messages are end-to-end encrypted. No one outside this chat can read or listen to them. Tap to learn more."
- Visual: light background pill, no avatar, no timestamp, center-aligned text (12pt regular, secondary label).
- Tap to open a sheet explaining the encryption + safety number / verification flow.

**Verification**:
- Safety number / verification code, displayed as a QR code + 60-digit number.
- Both parties can scan each other's QR to verify out-of-band. Animate the QR appearing with a Vision-framework subject-lifting style shimmer.

**Lock icon in nav**:
- Subtle 12pt lock icon next to the chat title, tinted secondary.
- For unverified contacts: tinted system orange. Tap to see "Verify safety number?" prompt.

### 14. Call experiences (audio & video)

**Outgoing call**:
- Full-screen native CallKit UI (use `CXProvider` + `CXCallController`). This is critical — your call appears in the system call log, on the lock screen, with Bluetooth controls.
- Custom in-app pre-call screen: avatar centered (120pt circle), name below (28pt semibold), "Calling..." subtitle, animated wave rings emanating from the avatar (CAReplicatorLayer for the rings).

**Incoming call**:
- Use CallKit's native incoming UI. Apple won't approve apps that try to override this.
- Pair with PushKit (VoIP push) for instant ring even when the app is suspended/killed.

**In-call UI** (when user enters the call screen):
- Top: tiny FaceTime/audio waveform indicator.
- Center: large avatar OR self-camera PiP.
- Bottom: mute / video / speaker / end call (large red circle) — standard 4-button row, with 64pt tap targets.

**Live Activity for ongoing call**:
- When the user backgrounds the app, surface a Live Activity (Dynamic Island on iPhone 14 Pro+):
  - Compact: speaker icon + call duration.
  - Expanded: avatar + name + duration + mute toggle + end call.

```swift
import ActivityKit

struct CallAttributes: ActivityAttributes {
    public struct ContentState: Codable, Hashable {
        var duration: TimeInterval
        var isMuted: Bool
    }
    var calleeName: String
    var calleeAvatarURL: URL
}

let activity = try Activity<CallAttributes>.request(
    attributes: CallAttributes(calleeName: "Sam", calleeAvatarURL: ...),
    content: .init(state: .init(duration: 0, isMuted: false), staleDate: nil),
    pushType: .token
)
```

### 15. Chat list (the conversation index)

**Cell layout:**
- 72pt tall (vertical).
- 56pt avatar on the left, 12pt right margin to content.
- Content area: vertically centered.
  - Top: chat title (17pt semibold) + timestamp (right-aligned, 13pt regular, secondary).
  - Bottom: last message preview (15pt regular, secondary label, 1 line truncation) + unread badge (right-aligned, blue circle with white count).
- Right-edge: chevron (`Image(systemName: "chevron.right")`, 12pt, tertiary tint).

**Avatar**:
- 56pt circle. For group chats: 4-grid mini-avatars OR custom emoji per the group's theme.
- Active-now indicator: 14pt green dot bottom-right with 2pt white border.

**Sorting**:
- Default: most-recently-active first.
- Pinned chats: pin icon to the right of the title; pinned chats are always at the top of the list with a subtle background tint.

**Unread state**:
- Bold text for title.
- Blue unread badge with count (system blue, 22pt height, dynamic width).
- For mention/reply: red @ badge instead of blue count.

**Swipe actions:**
- Swipe-left: Archive, Mute, Delete (red, terminal).
- Swipe-right: Pin, Mark as Read/Unread.
- Use `swipeActions(edge:)` in SwiftUI or `UISwipeActionsConfiguration` in UIKit.

**Search**:
- Pull down to reveal the search field.
- Recent searches above results.
- Search hits inline-highlight the matched substring in the preview.

---

## Animation curves cheat sheet

| Surface | Curve | Notes |
| --- | --- | --- |
| Bubble send (composer → list) | `.spring(response: 0.42, dampingFraction: 0.78)` | Slight overshoot, settles fast |
| Bubble receive | `.spring(response: 0.4, dampingFraction: 0.85)` | Subtler than send — your message arriving should be calm |
| Composer pill grow | `.linear` | Multi-line growth — NEVER spring, fights the keyboard |
| Mic ↔ send swap | `.spring(response: 0.32, dampingFraction: 0.7)` | Snappy, definite |
| Reaction pill appear | `.spring(response: 0.36, dampingFraction: 0.72)` | Bouncy |
| Reaction emoji stagger | `0.04s delay each` + same spring | Cascading |
| Reaction land on bubble | `.spring(response: 0.32, dampingFraction: 0.65)` | Bouncier — "stuck" |
| Long-press menu open | `.spring(response: 0.36, dampingFraction: 0.78)` | Match iMessage |
| Reply chip appear | `.spring(response: 0.32, dampingFraction: 0.85)` | Calm |
| Typing dots (each cycle) | `.easeInOut(duration: 0.45)` repeat | Standard |
| Chat list cell swipe | `.spring(response: 0.32, dampingFraction: 0.82)` | iOS-native feel |
| Push to chat detail | system push | Don't override |
| Modal sheet (e.g., contact info) | `.spring(response: 0.45, dampingFraction: 0.86)` | Standard sheet |
| Call screen present | `.spring(response: 0.5, dampingFraction: 0.92)` | Slightly slower — gravity |

**Reduce Motion**: replace springs with `.easeInOut(duration: 0.18)` crossfades, kill stagger, skip message effects.

---

## Haptics cheat sheet

| Action | Generator | Style | Notes |
| --- | --- | --- | --- |
| Tap send | `UIImpactFeedbackGenerator` | `.light` | Prepare in `keyboardWillShow` |
| Message delivered (confirmation) | none | — | Don't haptic on every delivery — too much noise |
| Message read (first time per session) | `UIImpactFeedbackGenerator` | `.soft` | One per conversation per session |
| Receive new message (foreground) | `UIImpactFeedbackGenerator` | `.soft` | Optional — many users find this jarring; opt-in |
| Long-press to open menu | `UIImpactFeedbackGenerator` | `.medium` | Fire on threshold cross |
| Pick reaction | `UIImpactFeedbackGenerator` | `.medium` | On tap |
| Reaction lands on bubble | `UIImpactFeedbackGenerator` | `.soft` | Fire when animation finishes |
| Mic ↔ send swap | `UISelectionFeedbackGenerator` | `.selectionChanged` | Prepare on text changes |
| Voice record start | `UIImpactFeedbackGenerator` | `.medium` | On press-down |
| Voice record cancel (drag past threshold) | `UINotificationFeedbackGenerator` | `.warning` | One-shot |
| Voice record lock (drag up) | `UINotificationFeedbackGenerator` | `.success` | One-shot |
| Voice playback scrub | `UIImpactFeedbackGenerator` | `.soft` | Throttle to 100ms |
| Swipe-to-reply threshold | `UIImpactFeedbackGenerator` | `.soft` | On threshold cross only |
| Chat list swipe-action threshold | `UIImpactFeedbackGenerator` | `.soft` | On threshold |
| Delete confirmation | `UINotificationFeedbackGenerator` | `.warning` | When destructive action confirmed |
| Outgoing call initiated | `UIImpactFeedbackGenerator` | `.heavy` | One-shot |

**Custom haptic patterns** for delight:
- **Send a "slam" effect message**: use CoreHaptics with a sharp transient + continuous decay (think: a small explosion).
- **Bubble lands after a long send animation**: a tiny "tick-tick" pattern (two `.soft` impacts 80ms apart).

```swift
let engine = try CHHapticEngine()
try engine.start()

let pattern = try CHHapticPattern(events: [
    CHHapticEvent(eventType: .hapticTransient, parameters: [
        .init(parameterID: .hapticIntensity, value: 1.0),
        .init(parameterID: .hapticSharpness, value: 0.8)
    ], relativeTime: 0),
    CHHapticEvent(eventType: .hapticContinuous, parameters: [
        .init(parameterID: .hapticIntensity, value: 0.4),
        .init(parameterID: .hapticSharpness, value: 0.2)
    ], relativeTime: 0.05, duration: 0.4)
], parameters: [])

try engine.makePlayer(with: pattern).start(atTime: 0)
```

---

## Typography for chat UIs

| Surface | Font | Weight | Size | Notes |
| --- | --- | --- | --- | --- |
| Bubble text | SF Pro | `.regular` | 17pt | Use Dynamic Type via `.body` |
| Solo emoji (≤3) | system emoji | — | 48pt | Auto-scale when message is emoji-only |
| Timestamp (inline group) | SF Pro | `.regular` | 11pt | Tracking 0.2, secondary label color |
| Read receipt | SF Pro | `.regular` | 11pt | Secondary label, beneath last sent bubble |
| Chat title (header) | SF Pro | `.semibold` | 17pt | Truncate with middle ellipsis if long |
| Chat subtitle (online status) | SF Pro | `.regular` | 13pt | Secondary label |
| Composer text input | SF Pro | `.regular` | 17pt | NEVER use a different size — matches bubbles for WYSIWYG |
| Chat list title | SF Pro | `.semibold` (unread) / `.regular` (read) | 17pt | |
| Chat list preview | SF Pro | `.regular` | 15pt | Secondary label, 1-line truncation |
| Chat list timestamp | SF Pro | `.regular` | 13pt | Tertiary label |
| Unread badge | SF Pro | `.semibold` | 13pt | White on system blue |
| System message (e.g., "X joined") | SF Pro | `.regular` | 13pt | Center-aligned, secondary label |
| In-call name | SF Pro | `.semibold` | 28pt | White on dark background |
| In-call duration | SF Mono | `.regular` | 17pt | Monospace digits — they don't jitter |

**Always support Dynamic Type** via `.body`, `.callout`, `.caption`, etc. Test with extra-large accessibility sizes (AX5).

---

## Color & material

- **Sent bubble**: app's accent color. For iMessage parity: `Color(red: 0.0, green: 0.48, blue: 1.0)` (iMessage blue). For green-bubble nostalgia: `Color(red: 0.21, green: 0.78, blue: 0.35)` (SMS green).
- **Received bubble**: `Color(.tertiarySystemGroupedBackground)` (light), `Color(.systemGray5)` (dark).
- **Background of conversation**: `Color(.systemGroupedBackground)` (light), `Color(.systemBackground)` (dark). Telegram and WhatsApp use a subtle pattern/wallpaper — if you do this, make it OFF by default.

**Chat wallpapers done right.** If you offer wallpapers (Telegram/WhatsApp pattern), each one is layered:
1. **Base color** picked in OKLCH so all wallpapers share the same perceived brightness (no "this one is darker than that one" inconsistency).
2. **Subtle pattern OR MeshGradient** (iOS 18+) for organic richness — never a flat gradient, which BANDS on OLED behind bubbles.
3. **3–6% noise overlay** with `.blendMode(.overlay)` to eliminate banding and add film-grain texture.
4. **Bubble contrast check** — every wallpaper must keep both sent and received bubbles legible (WCAG AA against the background gradient at the bubble's edges, not just the center).

See `the-final-5-percent` §5 for the full OKLCH workflow and `MeshGradient` / noise overlay patterns. Apply the same hierarchy to wallpapers as to any premium background.
- **Composer background**: `Color(.systemBackground)` with a top border (`Color(.separator)`, 0.5pt).
- **Unread badge**: `Color(.systemBlue)`.
- **Failed/error**: `Color(.systemRed)`.
- **Mention highlight**: `Color(.systemYellow).opacity(0.18)` background tint on the bubble.

**iOS 26 Liquid Glass considerations**: if your overall app is using Liquid Glass surfaces, the composer and nav bar can pick up `.glassEffect()` modifiers. Bubbles themselves should remain solid — glassy bubbles destroy readability and the conversational hierarchy.

---

## Novel iOS APIs to consider

This is where you separate the chat app from the *iOS* chat app.

### CallKit + PushKit (table stakes for any calling feature)
- **CallKit**: integrates your audio/video calls into the system UI. The call shows up in the lock-screen call UI, the call history, and respects "Do Not Disturb / Focus" settings. NO chat app shipping calls in 2026 should not use CallKit.
- **PushKit**: VoIP push notifications wake your app even from a killed state to ring instantly. Critical: you MUST report the call to CallKit within 5 seconds of receiving the push, or Apple will throttle your VoIP push entitlement.

```swift
import PushKit
import CallKit

let pushRegistry = PKPushRegistry(queue: .main)
pushRegistry.desiredPushTypes = [.voIP]
pushRegistry.delegate = self

// In delegate:
func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, for type: PKPushType, completion: @escaping () -> Void) {
    let provider = CXProvider(configuration: CXProviderConfiguration(localizedName: "MyApp"))
    let update = CXCallUpdate()
    update.remoteHandle = CXHandle(type: .generic, value: payload.dictionaryPayload["caller"] as! String)
    provider.reportNewIncomingCall(with: UUID(), update: update) { error in completion() }
}
```

### Communication Notifications API (iOS 15+)
The system that puts your contact's AVATAR on the lock-screen notification with their NAME (not your app's name). Massively differentiating.

```swift
// In your Notification Service Extension:
let contactHandle = INPersonHandle(value: "alice@example.com", type: .emailAddress)
let person = INPerson(personHandle: contactHandle, nameComponents: nameComponents, displayName: "Alice", image: INImage(imageData: avatarPNG), contactIdentifier: nil, customIdentifier: nil, isMe: false, suggestionType: .none)
let intent = INSendMessageIntent(recipients: [me], outgoingMessageType: .outgoingMessageText, content: messageBody, speakableGroupName: nil, conversationIdentifier: chatID, serviceName: "MyApp", sender: person, attachments: nil)
let updatedContent = try request.content.updating(from: intent)
contentHandler(updatedContent)
```

### Notification Service Extension (for E2EE pushes)
Your push payload arrives encrypted; the NSE decrypts it locally before showing the notification. No server-side plaintext, even in the push pipeline. Signal/iMessage style.

### App Intents (iOS 16+)
Expose chat actions to Siri / Shortcuts / Spotlight:
- "Send message to Alice" with on-device intent resolution.
- "Read my unread messages from Bob".
- Create custom focus filters: "When I'm in Focus mode 'Family', only allow messages from family group."

```swift
struct SendMessageIntent: AppIntent {
    static var title: LocalizedStringResource = "Send a message"
    static var openAppWhenRun = false

    @Parameter(title: "Recipient")
    var recipient: ContactEntity

    @Parameter(title: "Message")
    var message: String

    func perform() async throws -> some IntentResult {
        await MessageStore.shared.send(message, to: recipient)
        return .result()
    }
}
```

### Live Activities + Dynamic Island
- **Ongoing call**: duration counter, mute toggle, end call.
- **Voice message receiving**: progress bar of the playback.
- **Group chat with active call**: who's currently talking (avatar in Dynamic Island leading region).
- **Self-destructing message countdown**: ticking timer in the Dynamic Island.

### Shared with You (iOS 15+)
When friends send you a link, photo, song, or app via Messages, it appears in the *target* app (Safari Reading List, Photos, Music, App Store) under a "Shared with You" section. To opt your app in for outgoing shares:

```swift
// In your share/send link logic:
let metadata = LPLinkMetadata()
metadata.originalURL = sharedURL
// ... attach to the Messages share
```

Conversely, if you build a target app (e.g., a podcast app), you can pull shared content via `SWHighlightCenter` (SharedWithYou framework).

### CryptoKit + Signal Protocol
- Use `Curve25519.KeyAgreement` for X25519 key exchange.
- `HKDF` for key derivation.
- `ChaChaPoly` (or `AES.GCM`) for symmetric encryption.
- Implement double-ratchet for forward secrecy.
- **DO NOT roll your own crypto.** Use libsignal-protocol-swift or audit your implementation thoroughly.

### Wallet / PassKit for in-chat payments
Send money in messages (iMessage Cash pattern): integrate `PKPaymentRequest` and surface a "Send $X to Alice" interactive bubble. Requires Apple Pay merchant entitlements.

### SharePlay (Group Activities)
Watch a video together, listen to music in sync, edit a doc collaboratively — all within a FaceTime/group chat context. `GroupActivities` framework. Hugely under-utilized by third-party messaging apps.

### App Clips
Let users join a group chat or accept a friend invite without installing the full app — they tap a link, get a 10MB App Clip, and can chat for a session. Critical for viral growth.

### Translation framework (iOS 17.4+)
Inline message translation. Long-press a bubble → "Translate" → on-device translation appears beneath. Configure source/target languages per chat in settings.

```swift
import Translation

struct ChatBubble: View {
    @State private var configuration: TranslationSession.Configuration?
    @State private var translatedText: String?

    var body: some View {
        Text(translatedText ?? message.text)
            .translationTask(configuration) { session in
                let response = try await session.translate(message.text)
                translatedText = response.targetText
            }
    }
}
```

### Speech framework (on-device, iOS 13+)
Auto-transcribe voice messages on the receiver's device. Set `recognizer.requiresOnDeviceRecognition = true` for privacy and offline support.

### VisionKit DataScannerViewController
Scan a QR code to add a contact, join a group, verify safety numbers. Apple's native scanning UI handles all the camera and detection logic.

### TipKit (iOS 17+)
Discoverability for hidden gestures (swipe-right-to-reply, long-press-to-react, voice-message-lock). Use `TipView` to surface these at the right moment — never on first launch (overwhelming), but after the user has had 5+ conversations.

### Symbol Effects (iOS 17+)
- `.symbolEffect(.bounce, value: trigger)` on the send arrow when a message lands.
- `.symbolEffect(.pulse)` on the typing indicator.
- `.symbolEffect(.variableColor)` on the recording mic for a chasing-light effect.

### Background URL Session for media
Voice messages, images, videos sometimes need to upload while the user backgrounds the app. Use `URLSessionConfiguration.background(withIdentifier:)` to keep transfers alive. Particularly important for long voice messages (30s+) and HD video.

### LinkPresentation for rich previews
Auto-generate rich link previews in bubbles using `LPLinkView` + `LPMetadataProvider`. Cache aggressively (LRU of ~200 entries).

### Communication Limits (Screen Time integration)
For family-friendly apps: integrate `FamilyControls` framework to respect Screen Time communication limits (children can only message approved contacts during certain hours).

### NetworkExtension (for private routing)
Build a per-app VPN that routes only your messaging traffic through a privacy-preserving relay (Signal/Apple iCloud Private Relay style).

### Spotlight + CSSearchableItem
Make conversations searchable via system Spotlight. Each chat and recent message becomes a `CSSearchableItem` indexed in Core Spotlight. Users find conversations via the home-screen pull-down search.

### Continuity / Handoff
Start a message on iPhone, finish on Mac. Implement `NSUserActivity` for chat detail views. Critical for cross-device users.

---

## Anti-patterns to avoid

1. **Animating every received message into view.** Users scrolling through 200 messages should not endure 200 spring animations. Only animate the latest message(s) that arrive while the chat is open.
2. **Showing read receipts by default.** This is a privacy and emotional load you're imposing. Make it opt-in (Signal/Telegram pattern).
3. **A composer that grows ABOVE 5 lines without scrolling.** It eats the conversation. Cap at 5 lines, then scroll inside.
4. **Pull-down to refresh in a chat list.** The chat list updates via push. Pull-down should reveal search.
5. **A typing indicator that survives forever.** If you see "Alice is typing..." for 2 minutes, the indicator is lying. Auto-hide after 3 seconds of no activity.
6. **Tying the bubble color to the user's avatar color.** Tempting (looks personalized!) but destroys the WHO-said-WHAT visual hierarchy. Stick with two colors: sent and received.
7. **Showing every "Alice joined the group" as a regular bubble.** Use a center-aligned system message style — neutral background, secondary text, no avatar.
8. **Implementing custom call UI instead of CallKit.** Apple will reject the app. Just use CallKit.
9. **Notification banners that say "New message" without the contents.** Either show the actual message (with sensible privacy settings) or use Communication Notifications to show "Alice" with their avatar. "New message" is useless.
10. **Bringing up a full-screen modal for emoji picking.** The keyboard is sacred. Reactions and stickers should appear ABOVE the keyboard or in a partial sheet — never replace the conversation view entirely.

---

## Privacy & safety

Messaging apps have an outsized responsibility for user safety. Bake these in from day one:

- **Block & report**: long-press a chat in the list → Block. The blocked user can't message you, can't see your online status, and gets a generic "unable to deliver" if they try.
- **Verify contact**: safety-number / QR verification for E2EE chats.
- **Screenshot detection** in sensitive conversations (view-once, ephemeral). Notify the other party.
- **Auto-delete** as a chat-level toggle.
- **Hidden chats** (PIN-protected): a folder of chats requiring biometric auth to view. Telegram's "Secret Chats" pattern.
- **Disappearing media metadata**: strip EXIF, location, device info from photos/videos before sending. NEVER ship a feature where a user might unintentionally share their home GPS.
- **Photo proof** (optional): cryptographic provenance for photos sent in-chat (Content Authenticity Initiative, C2PA).
- **Communication Safety** (iOS 17+): use the system API to blur sensitive images for minor accounts.

---

## Performance bar

Anything below these numbers is unacceptable for a chat app shipping in 2026:

| Metric | Bar |
| --- | --- |
| Cold-start to chat list | ≤ 700ms |
| Tap chat → conversation visible & scrollable | ≤ 200ms |
| Tap send → bubble appears in conversation | ≤ 50ms (optimistic) |
| Receive push → message visible in app | ≤ 400ms when app is foregrounded |
| Voice message recording latency (press → mic active) | ≤ 80ms |
| Scroll FPS in conversation | 60fps (120fps on ProMotion) |
| Memory in a 10k-message conversation | < 200MB |
| Push payload size (E2EE) | < 4KB |

Profile with Instruments: especially **SwiftUI** template for view-update churn, **Network** for RTT and payload sizes, **Animation Hitches** for jank.

---

## Implementation checklist for a new chat app

- [ ] **Chat list** with avatar, title, last message, timestamp, unread badge, swipe actions.
- [ ] **Conversation view** with grouped bubbles, tails, avatars on received-only-last-of-group.
- [ ] **Composer** with auto-growing input, attachment +, mic ↔ send swap, keyboard tracking.
- [ ] **Send animation** with optimistic UI + retry on failure.
- [ ] **Receive** with subtle entry animation and `.soft` haptic.
- [ ] **Reactions** via long-press → reaction pill → tap to apply.
- [ ] **Context menu** with Reply, Copy, Forward, Pin, Delete, Edit (15min window).
- [ ] **Swipe-right to reply** with haptic + reply chip in composer.
- [ ] **Voice messages**: hold-to-record, slide-to-cancel, slide-up-to-lock, live waveform, playback bubble with scrub.
- [ ] **Typing indicator** with 3-dot animation, 2.5s timeout.
- [ ] **Read receipts** (off by default, with privacy tiers).
- [ ] **Presence** (online / last-seen / status).
- [ ] **Group chat creation**: pick people, customize, emoji avatar, color.
- [ ] **CallKit** integration for audio/video.
- [ ] **PushKit** for VoIP push.
- [ ] **Notification Service Extension** for E2EE decryption + Communication Notifications avatars.
- [ ] **CryptoKit / Signal protocol** for E2EE.
- [ ] **Live Activity** for ongoing calls + receiving voice messages.
- [ ] **App Intents** for Siri integration ("Send message to X").
- [ ] **Translation framework** for inline translation.
- [ ] **Speech framework** for voice-message transcription.
- [ ] **Shared with You** for outgoing links/media.
- [ ] **Reduce Motion** alternative paths for all spring animations.
- [ ] **Dynamic Type** support across all text.
- [ ] **Reduce Transparency** opaque background variants.
- [ ] **Increase Contrast** higher-contrast borders and text.
- [ ] **VoiceOver** accessibility labels on every interactive element.
- [ ] **Reachable** for one-handed use (chat list cells reachable in iPhone Pro Max range).
- [ ] **Privacy**: block, report, auto-delete, ephemeral, view-once, EXIF stripping.

---

## Final principles

1. **The composer is the product.** Everything else is supporting cast.
2. **Optimistic UI is mandatory.** Show the bubble before the network responds. Reconcile later.
3. **Bubbles tell a story.** Grouping, spacing, and tail placement carry as much meaning as the text.
4. **Reactions over replies.** A reaction is 10× faster than typing back. Make them effortless.
5. **Latency is intimacy.** A message that arrives 100ms faster feels 10× more "alive". Optimize the read path.
6. **Privacy is a feature.** Read receipts off by default. Ephemeral built-in. Encryption visible.
7. **Respect the keyboard.** It's the user's primary input. Never push it around or replace it lightly.

The benchmark: a user opens your chat app to send a quick message and finds themselves typing in < 1 second from tap, watching the bubble fly into the conversation, and putting their phone down. They don't remember what your app looks like — only that they felt heard. That's the goal.


---

## iOS Interaction Primitives (Widgets, Live Activities, Haptics)

_When to use this section: Design and build best-in-class native iOS interaction surfaces — Home Screen widgets, Lock Screen widgets, StandBy widgets, Live Activities, Dynamic Island presentations, Control Center custom controls, Haptic Touch context menus, haptic feedback (UIFeedbackGenerator and CoreHaptics), Action Button, Camera Control button, App Intents, Symbol Effects, and Focus filters. Use this skill whenever the user is building or polishing any of these peripheral surfaces that surround a native iOS app, especially for apps targeting iOS 17, iOS 18, or iOS 26 (Liquid Glass). Triggers on: widget, WidgetKit, TimelineProvider, Home Screen widget, Lock Screen widget, StandBy widget, interactive widget, widget toggle, widget button, App Intent, AppIntent, ControlWidget, Control Center widget, ControlWidgetButton, ControlWidgetToggle, Live Activity, ActivityKit, Dynamic Island, compact presentation, expanded presentation, minimal presentation, lock screen presentation, ActivityAttributes, Live Activity push, push token update, Communication Notifications, Haptic Touch, long press, context menu, UIContextMenuInteraction, peek and pop, 3D Touch, haptic feedback, UIImpactFeedbackGenerator, UISelectionFeedbackGenerator, UINotificationFeedbackGenerator, CoreHaptics, CHHapticEngine, CHHapticPattern, CHHapticEvent, AHAP, custom haptic, haptic AHAP, Action Button, Camera Control, half press, full press, Symbol Effects, symbolEffect, bounce, pulse, variableColor, Focus filters, FocusFilterIntent, sensitive content analysis, Live Text, App Shortcuts, Siri Shortcuts, iOS 26, Liquid Glass widget, glassEffect._

# iOS Interaction Primitives — Design Engineering Skill

A taste guide for the *peripheral* surfaces that surround a native iOS app — the Home Screen widget, the Dynamic Island, the haptic pulse on a button press. These are not afterthoughts. For many users, these surfaces are the *primary* product. Spotify's widget gets opened 50× more often than the app. Flighty's Dynamic Island is more memorable than Flighty's main screen.

## Philosophy

> The app is the universe. The widget is the planet you see from your bed.

Three rules that govern every primitive in this guide:
1. **Glanceability is the entire design constraint.** A widget that takes 2 seconds to parse is broken. Lock-Screen widgets get 0.4 seconds of attention. Dynamic Island gets less. Design for the half-second.
2. **One App Intent, many surfaces.** Since iOS 17, the same `AppIntent` powers Home widgets, Lock widgets, StandBy, Control Center, the Action Button, and Siri. Architect your business logic around intents — your peripheral surfaces become near-free.
3. **Haptics are punctuation, not paragraphs.** They confirm, they don't communicate. The wrong haptic feels like the app yelling. The right haptic feels like the app *agreeing* with you.

The pixel-pushers' rules:
- **Widgets are content, not chrome.** No "Open in app" buttons, no settings gears, no logos. The data IS the widget.
- **Live Activities live and die.** Set a `staleDate`. End them within 8 hours. Never leave a stale Activity hanging.
- **The Dynamic Island is a canvas, not a wallpaper.** No background colors, no images that bleed to the edge — Apple's HIG is explicit: foreground elements only.
- **Default haptics are not optional.** Every tappable thing in your app should fire a haptic. If you're not sure which, use `.selectionChanged`. It's never wrong.

---

## What this skill covers

| Surface | Framework | Min iOS | Section |
| --- | --- | --- | --- |
| Home Screen widgets | WidgetKit + SwiftUI | 14 (16 for Lock, 17 for interactive) | [§1](#1-home-screen-widgets) |
| Lock Screen widgets | WidgetKit | 16 | [§2](#2-lock-screen-widgets) |
| StandBy widgets | WidgetKit | 17 | [§3](#3-standby-widgets) |
| Live Activities (Lock Screen) | ActivityKit | 16.1 | [§4](#4-live-activities) |
| Dynamic Island | ActivityKit (DynamicIsland) | 16.1 (iPhone 14 Pro+) | [§5](#5-dynamic-island) |
| Control Center custom controls | WidgetKit (ControlWidget) | 18 | [§6](#6-control-center-custom-controls) |
| Haptic Touch context menus | UIContextMenuInteraction / `.contextMenu` | 13 | [§7](#7-haptic-touch--context-menus) |
| UIFeedbackGenerator haptics | UIKit | 10 | [§8](#8-haptic-feedback-the-easy-90) |
| Core Haptics (custom patterns) | CoreHaptics | 13 | [§9](#9-core-haptics-the-delightful-10) |
| Action Button | App Intents | 17 (iPhone 15 Pro+) | [§10](#10-action-button-iphone-15-pro) |
| Camera Control button | AVFoundation | 18 (iPhone 16/16 Pro) | [§11](#11-camera-control-button-iphone-16) |
| Symbol Effects | SwiftUI | 17 | [§12](#12-symbol-effects) |
| Focus filters | AppIntents | 16 | [§13](#13-focus-filters) |

---

## Reference apps to study

Premium examples of each surface, with Mobbin citations:

| App | What to learn | Mobbin |
| --- | --- | --- |
| **Flighty** | Best-in-class Dynamic Island for flight tracking — compact (countdown), expanded (full status), live updates throughout journey | [Flighty Dynamic Island](https://mobbin.com/screens/cfd5bf7f-efe2-4a72-a8ba-84302dc5c331), [delay state](https://mobbin.com/screens/0c6d9f54-f050-488d-92d4-c0fbeeed6901) |
| **FocusFlight** | Lock Screen Live Activity for flights — large rectangular widget with route/ETA/timezone, never feels cluttered | [FocusFlight LA](https://mobbin.com/screens/54d63fe8-f924-436c-9071-c63038dbefb6) |
| **Runbuds** | Workout Live Activity — distance, pace, time with red accent, no chrome | [Runbuds DI](https://mobbin.com/screens/4902bd7a-b3c6-473a-a9c0-af8be91ff5b4), [Lock Screen](https://mobbin.com/screens/8ebcad43-ccca-4a8e-81c2-70a0496a0393) |
| **Moonlitt / Sunlitt** | Beautiful gradient-backed Lock Screen widgets for moon/sun phases — content as art | [Moonlitt Lock](https://mobbin.com/screens/cee3304b-1709-427f-8ac4-7df615080050), [Sunlitt Golden Hour](https://mobbin.com/screens/dfe1dd5e-2194-45d0-bd1c-72484fc92956) |
| **Duolingo** | Streak widget on Lock Screen + Dynamic Island variants — emotional hook (the sad owl when streak is in danger) | [Streak widget](https://mobbin.com/screens/c78046b1-5d17-4225-ad76-2d66a72ac8bd) |
| **Yazio** | Lock Screen Live Activity for tracking meals — 4 ring meters in one strip | [Yazio Lock Screen](https://mobbin.com/screens/4bc38d1d-5a05-4e0a-8939-352891988c19) |
| **Transit** | Real-time bus arrival Live Activity — countdown with route color | [Transit Lock](https://mobbin.com/screens/b84f786b-1c21-4110-9977-f0544d9adcf5) |
| **MyFitnessPal / Yazio / Alma / GO Club** | Interactive widgets for logging water, calories, steps — tap to log without opening the app | [MFP Water widget](https://mobbin.com/screens/f74772bf-95d0-4a91-8e2d-56d33a77508e), [Alma Carrot](https://mobbin.com/screens/fe23c4a3-b043-432c-aa9f-9bb4db519889) |
| **TIDE / Tolan** | Minimal Dynamic Island for ambient apps (timers, AI characters) | [TIDE](https://mobbin.com/screens/4d286ed5-f515-4bd7-aa63-2bb579b8030b), [Tolan Lock Screen](https://mobbin.com/screens/a0693172-1a6d-4e4b-80b9-f8a29980cc4f) |
| **Apple Music / Maps / Timer** | The system standard for Live Activities. Study them on your device — they're the bar. | (use your device) |

---

## 1. Home Screen widgets

Widgets are SwiftUI views rendered by the system from your `TimelineProvider`. They cannot animate continuously; they redraw at intervals you specify.

### Sizing

| Size | Use case |
| --- | --- |
| `.systemSmall` (2×2 grid) | A single number / status (steps today, weather temp, streak count) |
| `.systemMedium` (4×2) | A title + 1–2 supporting data points, OR a horizontal bar chart |
| `.systemLarge` (4×4) | A list of items (up next 3 calendar events, top 5 tasks) |
| `.systemExtraLarge` (iPad only) | A dashboard view |
| `.accessoryCircular`, `.accessoryRectangular`, `.accessoryInline` | Lock Screen and StandBy widgets |

### Layout grid

- 22pt margins inside `.systemSmall` and `.systemMedium`.
- 24pt margins inside `.systemLarge`.
- 8pt content gap (between title and primary data).
- Corner radius: handled by the system. Use `ContainerRelativeShape()` to follow the widget's outer shape for inner elements (cards, backgrounds).

```swift
RoundedRectangle(cornerRadius: 22, style: .continuous) // ❌ Wrong
ContainerRelativeShape()                                // ✅ Right
```

### Typography for widgets

The single most common widget mistake: text too small to read at arm's length. Bars:

| Element | Font | Weight | Size |
| --- | --- | --- | --- |
| Hero number | SF Pro Rounded | `.bold` | 36pt (small) / 48pt (medium) / 64pt (large) |
| Hero label | SF Pro | `.semibold` | 13pt |
| Supporting metric | SF Pro | `.medium` | 15pt |
| Caption / timestamp | SF Pro | `.regular` | 11pt |

Always set `.minimumScaleFactor(0.7)` on hero numbers to handle internationalization gracefully (12,345 km is wider than 1.2 mi).

### Refresh cadence

Widgets are NOT push-driven. The system reads your timeline.

- Budget: roughly 40–70 reloads per day across all your widgets per device.
- For frequent updates, return a longer timeline (e.g., 24 entries spaced 1 hour apart) so the system has data to render between actual reloads.
- For sparse updates (e.g., delivery tracking that changes 4 times a day), use `WidgetCenter.shared.reloadTimelines(ofKind:)` from the app or a background task.

```swift
struct CoffeeWidgetProvider: TimelineProvider {
    func getTimeline(in context: Context, completion: @escaping (Timeline<CoffeeEntry>) -> Void) {
        let entries = generateNextHourEntries() // 12 entries, 5min apart
        let timeline = Timeline(entries: entries, policy: .after(Date().addingTimeInterval(3600)))
        completion(timeline)
    }
}
```

### Interactive widgets (iOS 17+)

The killer feature. Same `AppIntent` powers widget buttons, Control Center, Action Button, Siri.

**Anatomy:**
- `Button(intent:)` or `Toggle(isOn:intent:)` — these render as SwiftUI controls and execute the intent in the background.
- The intent's `perform()` runs in the WIDGET extension's process, not your app's. Share data via App Groups.
- After the intent runs, the widget timeline refreshes — your UI updates with the new state.

```swift
import WidgetKit
import SwiftUI
import AppIntents

struct LogWaterIntent: AppIntent {
    static var title: LocalizedStringResource = "Log a glass of water"

    @Parameter(title: "Amount (ml)")
    var amount: Int

    func perform() async throws -> some IntentResult {
        await WaterStore.shared.log(amount: amount) // shared via App Group
        return .result()
    }
}

struct WaterWidgetView: View {
    let entry: WaterEntry
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Image(systemName: "drop.fill").foregroundStyle(.blue)
                Text("Water").font(.system(size: 13, weight: .semibold))
            }
            Text("\(entry.totalToday) ml")
                .font(.system(size: 36, weight: .bold, design: .rounded))
                .contentTransition(.numericText(value: Double(entry.totalToday)))
            Button(intent: LogWaterIntent(amount: 250)) {
                Label("+250 ml", systemImage: "plus")
                    .font(.system(size: 13, weight: .semibold))
            }
            .buttonStyle(.borderedProminent)
            .tint(.blue)
        }
        .containerBackground(.fill.tertiary, for: .widget)
    }
}
```

**Animation in widgets**: limited but lovely.
- `.contentTransition(.numericText(value:))` — rolls digits like an odometer when numbers change.
- `.contentTransition(.symbolEffect)` — bounces SF Symbols on state change.
- `withAnimation` works inside intent callbacks — the system animates the diff between widget states.

### iOS 26 Liquid Glass widgets

iOS 26 widgets adopt the Liquid Glass material. To opt in:
- Set `.containerBackground(.fill.tertiary, for: .widget)` — the system picks the right material per context.
- Use `.widgetAccentable()` on elements you want tinted in Accent rendering mode (the user can choose between Auto / Accent / Light / Dark tint per widget).
- Avoid hardcoded colors for backgrounds; use semantic system colors so they adapt.
- For dark accent on light wallpaper / vice versa, use `.foregroundStyle(.primary)` and let the system handle contrast.

```swift
Text("\(entry.steps)")
    .font(.system(size: 48, weight: .bold, design: .rounded))
    .widgetAccentable() // gets tinted in Accent mode
```

### MeshGradient for premium Home Screen widgets (iOS 18+)

For brand-defining widgets where the background IS part of the personality (workout apps, finance apps, music apps), use `MeshGradient` as the container background. It looks hand-painted and renders for free.

```swift
struct PremiumWidget: View {
    let entry: Entry
    var body: some View {
        VStack(alignment: .leading) {
            Text("\(entry.value)")
                .font(.system(size: 48, weight: .bold, design: .rounded))
                .foregroundStyle(.white)
            Text("Today").font(.caption).foregroundStyle(.white.opacity(0.8))
        }
        .containerBackground(for: .widget) {
            MeshGradient(
                width: 2, height: 2,
                points: [[0,0], [1,0], [0,1], [1,1]],
                colors: [.indigo, .purple, .pink, .orange]
            )
        }
    }
}
```

**Rules:**
- **Home widgets only.** Lock Screen widgets render in tint-mode (monochrome) — MeshGradient gets flattened and looks broken. Use `.containerBackground(.fill.tertiary, for: .widget)` (semantic) for Lock variants.
- **Dynamic Island is forbidden from backgrounds.** Apple's HIG: foreground elements only. Never apply MeshGradient or any background fill to a Dynamic Island presentation.
- **Pick colors in OKLCH** so the mesh feels balanced rather than chaotic. See `the-final-5-percent` §5.
- **Keep text high-contrast.** A MeshGradient background means dynamic colors behind your text. Add a subtle shadow or use `.foregroundStyle(.white)` with a translucent darkening layer if needed for legibility.

### Anti-patterns
- **Don't put a "Open App" button.** Tap-anywhere-to-open is automatic. Buttons should DO things.
- **Don't fill the widget with chrome.** Top label + giant data point + maybe one secondary element. That's it.
- **Don't update a sleeping widget.** If nothing's changed, return a long-tail timeline. Updating just to update wastes the budget.
- **Don't use thin fonts.** SF Pro Light at any size looks fine on a high-DPI display in your editor and unreadable on a Lock Screen at arm's length.

---

## 2. Lock Screen widgets

Three sizes, all monochrome, all tiny. Treat them as iconography, not data viz.

| Family | Size | Use case |
| --- | --- | --- |
| `.accessoryCircular` | ~76 × 76pt rendered | A single number, a gauge, a progress ring |
| `.accessoryRectangular` | ~160 × 76pt rendered | A title + one line of supporting info |
| `.accessoryInline` | Single text line beside time | "Coffee: 3 cups", "Next: Sam 14:30" |

### Visual language

Lock Screen widgets render in **tint mode** by default — flat single-color silhouettes (the user's chosen tint). You can render in **full color** by setting `.widgetRenderingMode(.fullColor)` but this is rarely the right call — full color photos on the Lock Screen look out of place and Apple actively discourages it.

Design rules:
- **Use SF Symbols** for icons (they tint correctly).
- **Use Gauge** for progress (built-in, looks native).
- **NO drop shadows or gradients** in tint mode — they're flattened to a single color and look weird.
- **Use `.privacySensitive()`** on data you don't want shown when the device is locked (Apple Watch only honors this currently, but it's good practice).

```swift
struct StreakLockWidget: View {
    let entry: StreakEntry
    var body: some View {
        VStack {
            Image(systemName: "flame.fill")
                .font(.system(size: 18))
            Text("\(entry.days)")
                .font(.system(size: 22, weight: .bold, design: .rounded))
                .contentTransition(.numericText())
            Text("days").font(.system(size: 9))
        }
    }
}
```

### Tap behavior

Tapping a Lock-Screen widget opens the app to a specific destination. Use `widgetURL`:

```swift
WaterLockWidgetView(entry: entry)
    .widgetURL(URL(string: "myapp://water/today")!)
```

OR — in iOS 17+ — make the entire widget a `Button(intent:)`. The intent fires, the app does NOT open. Use this for "increment my coffee count from the Lock Screen" UX.

---

## 3. StandBy widgets

When iPhone is plugged in and on its side (iOS 17+), it enters StandBy mode. Your widget appears in a special context: nighttime-friendly, glanceable from across a room.

- StandBy uses `.systemSmall` widgets by default in a stacked carousel.
- At night, the system shifts to **Red Tint mode** automatically — your widget gets a red monochrome rendering. SF Symbols and text re-tint correctly; gradient/photo backgrounds get clipped.
- Always design the small widget to look great at 6 feet away. That's the test.

Design rules for StandBy:
- Hero number ≥ 56pt.
- High contrast — white on black, or your accent on dark.
- No interactive buttons in StandBy (taps just open the app).
- Test red-tint mode! Most apps haven't and look terrible.

---

## 4. Live Activities

Live Activities display real-time data on the Lock Screen and Dynamic Island. They survive in the system for up to 8 hours (with caveats — iOS 17.2+ allows extension).

### When to use them

✅ Sports score in progress
✅ Food delivery / rideshare ETA
✅ Workout in progress
✅ Timer / Pomodoro
✅ Flight tracker
✅ Audio call / FaceTime
✅ Long-running export / upload

❌ Background processes the user doesn't care about minute-to-minute
❌ Daily check-ins ("Don't forget your meditation!")
❌ Marketing / promotions
❌ "Hey, look at me!" — be a tool, not a billboard

### Anatomy

You define:
1. `ActivityAttributes` — static info that doesn't change (e.g., "Flight DL 412 SFO → JFK").
2. `ContentState` — dynamic info that updates (e.g., gate, delay status, ETA).
3. **Four presentations**:
   - **Lock Screen** (large rectangular widget on Lock Screen + Notification Center)
   - **Dynamic Island compact** (leading + trailing islands when only your activity is showing)
   - **Dynamic Island expanded** (when user touches and holds the Island)
   - **Dynamic Island minimal** (a tiny icon when multiple activities are competing)

```swift
struct FlightAttributes: ActivityAttributes {
    public struct ContentState: Codable, Hashable {
        var status: FlightStatus  // boarding, departed, in-flight, landed
        var minutesRemaining: Int
        var gate: String?
    }
    var flightNumber: String
    var origin: String
    var destination: String
}

struct FlightLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: FlightAttributes.self) { context in
            // Lock Screen presentation
            FlightLockView(context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                // Expanded
                DynamicIslandExpandedRegion(.leading) { ... }
                DynamicIslandExpandedRegion(.trailing) { ... }
                DynamicIslandExpandedRegion(.bottom) { ... }
            } compactLeading: {
                Image(systemName: "airplane")
            } compactTrailing: {
                Text(context.state.minutesRemaining, format: .number) + Text("m")
            } minimal: {
                Image(systemName: "airplane")
            }
            .keylineTint(.green) // border tint
        }
    }
}
```

### Lock Screen Live Activity design

- Max height: ~160pt (the system gives you up to this; respect it).
- Layout in tiers:
  - **Top row**: app icon (left) + title + status pill (right). 24pt height.
  - **Middle**: the hero content. A route map, a giant timer, a progress bar.
  - **Bottom row**: secondary info — gate, ETA, delta vs schedule. 20pt height.
- Use `.activityBackgroundTint(.black)` for the background or let it inherit the Lock Screen wallpaper context.
- Honor Dynamic Type via `.body`, `.caption`, etc.

**Flighty's lock-screen activity** is the reference. Study it.

### Updating from your server

Live Activities can be push-updated. Get the push token after starting the activity:

```swift
let activity = try Activity<FlightAttributes>.request(
    attributes: ...,
    content: .init(state: ..., staleDate: Date().addingTimeInterval(4 * 3600)),
    pushType: .token
)

Task {
    for await tokenData in activity.pushTokenUpdates {
        let tokenHex = tokenData.map { String(format: "%02x", $0) }.joined()
        await uploadToken(tokenHex, for: activity.id)
    }
}
```

Then send pushes via APNs to `push-type: liveactivity`.

**Best-practice cadence**: update only when something *changed enough to notice*. For a flight: every 10 minutes during pre-boarding, every 2 minutes during taxi/approach. For a ride-share: every 30s while in transit. For audio playing: 5–10s.

### staleDate

Set `staleDate` aggressively. After this date, your activity becomes visually "stale" (slightly desaturated) until the next update. Users hate seeing 2-hour-old data presented as live.

### Ending Live Activities

```swift
await activity.end(
    ActivityContent(state: finalState, staleDate: nil),
    dismissalPolicy: .after(Date().addingTimeInterval(60))
)
```

Three dismissal options:
- `.immediate`: removes from UI immediately.
- `.default`: keeps for ~4 hours after ending (user can swipe away).
- `.after(date)`: keeps until specified date (max 4 hours).

For "you've arrived" / "your timer's done" → `.after(now + 60s)` so the user sees the end state, then it disappears.

---

## 5. Dynamic Island

The Dynamic Island is a *canvas of foreground elements floating around the TrueDepth camera*. Apple's HIG is explicit: **no background colors, no images that bleed.**

### Three presentations

**Compact** (the default when only your activity is live):
- Two regions: **leading** (left of camera) and **trailing** (right of camera).
- Each region max ~50pt wide.
- Use a single icon + ≤ 5 characters of text per side.
- Leading: usually an icon representing the activity (airplane, fork, timer).
- Trailing: the most-glanceable data point (countdown, ETA, score).

**Minimal** (when multiple activities compete, or yours isn't most active):
- A SINGLE element — usually a 22 × 22pt icon.
- Two minimal activities show side by side, one "attached" to the Island, one floating just below it.

**Expanded** (when user touches-and-holds the Island):
- Four regions: `.leading`, `.trailing`, `.center`, `.bottom`.
- This is where you can show rich content: a map, progress rings, multiple lines of text, controls.
- Max height: ~200pt.
- **You CAN have buttons here** (interactive Live Activities, iOS 17+) — `Button(intent:)` etc.

### Design rules (these are not optional)

From Apple's HIG:
1. **No background colors.** The Island IS your background.
2. **No images that touch the edges.** Inset all visual elements with ≥ 4pt padding.
3. **No buttons in compact or minimal.** Interactive elements only in expanded.
4. **Use `.keylineTint(...)`** to add a subtle 1pt border tint around the entire Island — this is the ONLY chrome you get for branding. Use it sparingly.
5. **Honor sensitivity:** if the user has Reduce Motion on, skip transitions; if Reduce Transparency, you don't need to change anything (the Island is opaque already).

### Animation between states

Transitions between content states are automatic. To make them beautiful:
- Use `.contentTransition(.numericText())` for changing numbers — they roll like an odometer.
- Use `.symbolEffect(.bounce)` for SF Symbols that change.
- Use `.transition(.opacity)` for swappable views.
- **Avoid complex layout changes** between updates — the system animates between two snapshots, and big layout deltas look choppy.

### Compact → Expanded transition

When the user long-presses the Island, the system runs a smooth morph from compact to expanded. You DON'T animate this — the system does. Your job is to make the two views *related enough* that the morph feels natural. Keep iconography consistent. Keep colors consistent.

### Minimal presentation

When two activities compete, your activity might be shown minimal. Test this. Many apps look great in compact and weird in minimal because the icon they chose doesn't read at 22pt.

### Real-world examples to study (Mobbin)

- **Flighty** — compact: airplane icon + countdown. The countdown turns red as you approach departure. [→](https://mobbin.com/screens/cfd5bf7f-efe2-4a72-a8ba-84302dc5c331)
- **FocusFlight** — full Lock Screen activity with origin/destination/route line. [→](https://mobbin.com/screens/54d63fe8-f924-436c-9071-c63038dbefb6)
- **Runbuds** — compact: running figure + distance. Lock Screen: distance / time / pace in three big rows. [→](https://mobbin.com/screens/4902bd7a-b3c6-473a-a9c0-af8be91ff5b4)
- **TIDE** — minimal-style breathing visualization. Look at how restrained it is. [→](https://mobbin.com/screens/4d286ed5-f515-4bd7-aa63-2bb579b8030b)

---

## 6. Control Center custom controls

New in iOS 18. Control Center now hosts custom `ControlWidget`s — the same App Intent architecture as widgets.

### Two types

**`ControlWidgetButton`**: a one-shot tap action.
```swift
struct StartTimerControl: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(kind: "com.app.startTimer") {
            ControlWidgetButton(action: StartTimerIntent()) {
                Label("Start Timer", systemImage: "timer")
            }
        }
        .displayName("Start Timer")
        .description("Quickly start a 25-minute timer.")
    }
}
```

**`ControlWidgetToggle`**: a state with on/off.
```swift
ControlWidgetToggle(
    "Focus Mode",
    isOn: focusEnabled,
    action: ToggleFocusIntent()
) { isOn in
    Label(isOn ? "Focus On" : "Focus Off",
          systemImage: isOn ? "moon.fill" : "moon")
}
```

### Where Controls appear

- **Control Center** (the user adds them via the redesigned Control Center).
- **Lock Screen** (bottom corners — replace flashlight/camera).
- **Action Button** (user can assign your control to it).

This is the magic: ONE intent, ONE control declaration, THREE surfaces. iOS 26 even adds them to the home screen widget surface as a "small action" style.

### Visual design

Controls inherit a system-rendered chrome (rounded rectangle, system material background). You provide:
- A `Label` with `Image(systemName:)` + text.
- Optionally, a `controlWidgetActionHint(...)` for accessibility.
- For toggles: separate visual states for on/off (different icon, optionally different color).

Use SF Symbols. Custom icons can be embedded via asset catalog with `Image("MyCustomIcon")`, but SF Symbols render correctly across all surfaces (full color, tinted, monochrome).

---

## 7. Haptic Touch & context menus

**Note**: 3D Touch was deprecated in iOS 13. Modern devices use **Haptic Touch** — a long-press with haptic feedback. The API surface is `UIContextMenuInteraction` (UIKit) or `.contextMenu { ... }` (SwiftUI).

### Timing

- Default long-press duration: **0.5 seconds** (system standard).
- For chat reactions, FAST: **0.4 seconds** (iMessage).
- For destructive contexts, SLOW: **0.7 seconds** (e.g., long-press to enter delete mode).

You can't change the system's long-press threshold globally, but you can use a custom `LongPressGesture(minimumDuration:)` for in-app gestures.

### The Haptic Touch interaction

When the user touches and holds an element:
1. **0–500ms**: nothing happens visually. The element is "loading" the menu.
2. **500ms**: haptic `.medium` impact fires, the element subtly scales to 0.97 (signaling "menu coming").
3. **520ms**: the rest of the screen blurs (`.systemUltraThinMaterial` background), the element scales back to 1.02 and lifts (slight shadow), the context menu appears with a stagger animation.
4. **Release on menu item**: haptic `.medium`, item highlights, action fires.
5. **Release outside menu**: haptic `.soft`, menu dismisses.

The system handles ALL of this for you when you use the standard APIs.

### SwiftUI implementation

```swift
PhotoCell(image: photo)
    .contextMenu {
        Button("Save", systemImage: "square.and.arrow.down") {
            save(photo)
        }
        Button("Share", systemImage: "square.and.arrow.up") {
            share(photo)
        }
        Divider()
        Button("Delete", systemImage: "trash", role: .destructive) {
            delete(photo)
        }
    } preview: {
        // Optional: full-size preview that appears while menu is shown
        Image(uiImage: photo.fullSize)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(maxWidth: 300, maxHeight: 400)
    }
```

The `preview` closure is a fantastic discoverability trick — long-pressing a small thumbnail shows a giant preview while the menu is shown. Apple Photos does this with photos in the library.

### Custom context menu animations (iMessage / Telegram style)

For maximum control over the animation (like iMessage's bubble-lift-and-reaction-pill), implement `UIContextMenuInteraction` manually:

```swift
let interaction = UIContextMenuInteraction(delegate: self)
bubbleView.addInteraction(interaction)

// In the delegate:
func contextMenuInteraction(_ interaction: UIContextMenuInteraction,
                            configurationForMenuAtLocation location: CGPoint)
    -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil) {
        // Preview view — can be nil for no preview
        nil
    } actionProvider: { _ in
        let reply = UIAction(title: "Reply", image: UIImage(systemName: "arrowshape.turn.up.left")) { _ in ... }
        let copy  = UIAction(title: "Copy", image: UIImage(systemName: "doc.on.doc")) { _ in ... }
        let delete = UIAction(title: "Delete", image: UIImage(systemName: "trash"),
                              attributes: .destructive) { _ in ... }
        return UIMenu(children: [reply, copy, delete])
    }
}
```

For TRULY custom presentations (the reaction picker pill above the bubble), you'll need to manage the animation yourself outside `UIContextMenuInteraction` and use a `UIWindow` overlay. iMessage and Telegram do this — it's significant work.

### When NOT to use a context menu

- **Don't use context menus as the ONLY way to access a feature.** They're discoverability hell. Mirror the actions in a visible UI somewhere.
- **Don't put more than 6 items.** Cognitive overload. If you have 10 actions, group them or use a sheet.
- **Don't nest more than 1 level of submenus.** Users get lost.
- **Don't use them on items that are also tap-actionable in confusing ways.** Tapping a tweet opens it; long-pressing should reveal MORE actions, not the same one.

---

## 8. Haptic feedback — the easy 90%

`UIFeedbackGenerator` covers the vast majority of cases. Memorize this table:

| Generator | Styles | When |
| --- | --- | --- |
| `UIImpactFeedbackGenerator` | `.light` | Light touches, button taps, selection of light/inert items |
| | `.medium` | Standard tap on a meaningful control |
| | `.heavy` | Critical actions, slammed-into-place events |
| | `.soft` | (iOS 13+) Even softer than `.light` — perfect for ambient feedback like scrolling detents |
| | `.rigid` | (iOS 13+) Sharp click — perfect for ratchets, dial detents, toggle switches |
| `UISelectionFeedbackGenerator` | (single style) | Picker/scroll-wheel changes, segmented control changes, ANY selection change in a scrollable list |
| `UINotificationFeedbackGenerator` | `.success` | Task completed successfully (saved, sent, posted) |
| | `.warning` | About-to-be-destructive (delete confirmation) |
| | `.error` | Failed action (login wrong, network error) |

### The two rules of UIFeedbackGenerator

**Rule 1: `prepare()` BEFORE you'll need it.**

Without prepare, the haptic engine spins up on first fire, adding ~50ms latency. With prepare, latency is < 5ms. You'll hear the difference.

```swift
private let lightImpact = UIImpactFeedbackGenerator(style: .light)

func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
    lightImpact.prepare() // warm up
}

func buttonTapped() {
    lightImpact.impactOccurred() // fires in < 5ms
}
```

**Rule 2: A generator stays "warm" for ~2 seconds after `prepare()`.**

If you `prepare()` then wait 3 seconds before firing, you're back to cold. For continuous interactions (a slider you'll be firing every 100ms), call `prepare()` after each `.impactOccurred()` to keep it warm.

### Haptic intensity (iOS 13+)

`UIImpactFeedbackGenerator` supports `.impactOccurred(intensity: 0.5)` — values 0.0 to 1.0. Map this to gesture velocity for natural-feeling drag-snap interactions.

```swift
// Velocity-mapped haptic during a scrub gesture
let v = abs(scrubVelocity) / maxVelocity // 0…1
impactGen.impactOccurred(intensity: 0.3 + v * 0.7) // 0.3 floor, scales to 1.0
```

### Common haptic anti-patterns

❌ Firing haptics on EVERY scroll event. The result feels like a vibrating phone.
✅ Fire on detents, breakpoints, or thresholds — the "ticks" the user is aware of.

❌ Using `.heavy` for normal button taps. Feels aggressive.
✅ Default to `.light` or `.soft`. Reserve `.heavy` for genuinely heavy moments.

❌ Using `.warning` for routine messages. Now users ignore your warnings.
✅ Reserve `.error` and `.warning` for truly destructive paths.

❌ Forgetting to honor system settings. `UIDevice` does NOT expose a "haptics disabled" setting — but the system respects the user's Sounds & Haptics setting automatically. You don't need to check.

❌ Haptics on cold app launches. The first few seconds the engine is sleeping; haptics will lag.

---

## 9. Core Haptics — the delightful 10%

When `UIFeedbackGenerator` isn't enough — multi-step patterns, audio-synced haptics, intensity envelopes — use `CoreHaptics`. This is what separates premium apps from default apps.

### When to reach for CoreHaptics

- Custom multi-tap patterns (a "chk-chk-chk" film advance, a "thump-thump" heartbeat, a "whoosh-pop" balloon release).
- Haptics that sync with audio (vocal effects, music drops, sound-effect synchronized hits).
- Continuous haptics with dynamic intensity (a vehicle's vibration that ramps with speed in a game).
- Haptic event longer than 1 sec (UIFeedbackGenerator only supports transients).

### Capability check

```swift
guard CHHapticEngine.capabilitiesForHardware().supportsHaptics else { return }
```

iPhone 8 and later support it. iPads do NOT support haptics (touch on iPad has none). Always degrade gracefully.

### Two event types

- **`hapticTransient`**: a short impulse (~80ms). Has `intensity` (0–1) and `sharpness` (0–1).
- **`hapticContinuous`**: a sustained vibration up to 30 seconds. Same parameters + `duration`.

### A reusable engine wrapper

Don't recreate the engine for every haptic. Wrap it:

```swift
import CoreHaptics

final class HapticPlayer {
    static let shared = HapticPlayer()
    private var engine: CHHapticEngine?

    init() {
        guard CHHapticEngine.capabilitiesForHardware().supportsHaptics else { return }
        do {
            engine = try CHHapticEngine()
            engine?.stoppedHandler = { _ in /* restart on next play */ }
            engine?.resetHandler = { [weak self] in try? self?.engine?.start() }
            try engine?.start()
        } catch {
            print("Haptic engine init failed: \(error)")
        }
    }

    func play(pattern: CHHapticPattern) {
        guard let engine else { return }
        do {
            let player = try engine.makePlayer(with: pattern)
            try player.start(atTime: 0)
        } catch {
            print("Play failed: \(error)")
        }
    }
}
```

### Pattern: a "shutter" haptic

```swift
let click = CHHapticEvent(eventType: .hapticTransient, parameters: [
    .init(parameterID: .hapticIntensity, value: 1.0),
    .init(parameterID: .hapticSharpness, value: 0.9)
], relativeTime: 0)

let echo = CHHapticEvent(eventType: .hapticTransient, parameters: [
    .init(parameterID: .hapticIntensity, value: 0.4),
    .init(parameterID: .hapticSharpness, value: 0.3)
], relativeTime: 0.06)

let pattern = try CHHapticPattern(events: [click, echo], parameters: [])
HapticPlayer.shared.play(pattern: pattern)
```

### Pattern: a "heartbeat"

```swift
func heartbeatPattern(bpm: Double = 60) throws -> CHHapticPattern {
    let interval = 60.0 / bpm
    var events: [CHHapticEvent] = []

    for beat in 0..<8 {
        let t = Double(beat) * interval
        // Lub (strong)
        events.append(.init(eventType: .hapticTransient,
                            parameters: [.init(parameterID: .hapticIntensity, value: 1.0),
                                         .init(parameterID: .hapticSharpness, value: 0.4)],
                            relativeTime: t))
        // Dub (softer, 0.12s later)
        events.append(.init(eventType: .hapticTransient,
                            parameters: [.init(parameterID: .hapticIntensity, value: 0.6),
                                         .init(parameterID: .hapticSharpness, value: 0.4)],
                            relativeTime: t + 0.12))
    }
    return try CHHapticPattern(events: events, parameters: [])
}
```

### AHAP files

For complex patterns, write them as `.ahap` JSON files in your bundle and load:

```swift
let url = Bundle.main.url(forResource: "doorbell", withExtension: "ahap")!
let pattern = try CHHapticPattern(contentsOf: url)
```

AHAP format (Apple Haptic and Audio Pattern):
```json
{
  "Version": 1.0,
  "Pattern": [
    { "Event": { "Time": 0.0, "EventType": "HapticTransient",
                 "EventParameters": [
                   { "ParameterID": "HapticIntensity", "ParameterValue": 1.0 },
                   { "ParameterID": "HapticSharpness", "ParameterValue": 0.8 }
                 ]
    }},
    { "Event": { "Time": 0.15, "EventType": "HapticContinuous", "EventDuration": 0.4,
                 "EventParameters": [
                   { "ParameterID": "HapticIntensity", "ParameterValue": 0.5 },
                   { "ParameterID": "HapticSharpness", "ParameterValue": 0.3 }
                 ]
    }}
  ]
}
```

Apple ships a few sample `.ahap` files in the Core Haptics sample code — start there.

### Sharpness vs Intensity (the two knobs)

- **Intensity** (volume): how strong does it feel? Low intensity = barely perceptible. High = strong vibration.
- **Sharpness**: how *crisp* does it feel? Low sharpness = soft/dull thump (like a felt mallet on a drum). High sharpness = crisp click (like a fingernail on glass).

Most natural-feeling haptics live around:
- Tap/click: intensity 0.8–1.0, sharpness 0.6–1.0.
- Soft press: intensity 0.4–0.6, sharpness 0.2–0.4.
- Rumble: intensity 0.3–0.6, sharpness 0.0–0.2.

### Audio + haptic synchronization

`CHHapticEvent` has `hapticAudioCustom` (uses an embedded audio file). For deeply immersive moments (a sword-clash sound effect tied to a haptic), this is the only way to sync perfectly.

```swift
let audioParams: [CHHapticEventParameter] = [
    .init(parameterID: .audioVolume, value: 0.8),
    .init(parameterID: .audioPitch, value: 0.0)
]
let audioResource = try engine.registerAudioResource(URL(...))
let audioEvent = CHHapticEvent(audioResourceID: audioResource,
                                parameters: audioParams,
                                relativeTime: 0)
```

---

## 10. Action Button (iPhone 15 Pro+)

The Action Button replaces the mute switch on iPhone 15 Pro and later. Users assign actions to it via Settings.

### How your app participates

Two paths:
1. **App Shortcuts**: declare an `AppShortcut` and the user can map it to the Action Button.
2. **Shortcuts integration**: provide an `AppIntent`; user can build a Shortcut that triggers your intent, then assign the Shortcut to the Action Button.

```swift
import AppIntents

struct StartFocusSessionIntent: AppIntent {
    static var title: LocalizedStringResource = "Start Focus Session"
    static var openAppWhenRun = false  // important — instant action

    func perform() async throws -> some IntentResult & ProvidesDialog {
        let session = try await FocusStore.shared.startSession()
        return .result(dialog: "Focus session started for \(session.duration) minutes.")
    }
}

struct MyAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: StartFocusSessionIntent(),
            phrases: ["Start focus session in \(.applicationName)",
                      "Begin focus in \(.applicationName)"],
            shortTitle: "Start Focus",
            systemImageName: "moon.zzz"
        )
    }
}
```

### Design considerations

- **Make the action fast and self-contained.** The user pressed a physical button — they want INSTANT result, not "we're loading."
- **Provide audio/haptic feedback** because there's no visual confirmation that the action fired. A `UINotificationFeedbackGenerator().notificationOccurred(.success)` is appropriate.
- **For long-running actions**, kick off a Live Activity + Dynamic Island presentation so the user sees confirmation.
- **Don't require the app to be open.** Use `openAppWhenRun = false` whenever possible.

### What kinds of actions work well

✅ Toggle a state (start/stop a workout, mute/unmute notifications)
✅ Record (audio, video, photo — direct to library)
✅ Log (water intake, mood, custom event)
✅ Open a specific screen (e.g., barcode scanner)

❌ Anything that requires confirmation
❌ Anything that opens a settings page
❌ Multi-step flows

---

## 11. Camera Control button (iPhone 16/16 Pro)

A physical button on the right edge of iPhone 16 with a force sensor + capacitive surface. Detects:
- **Half-press** (force threshold 1): focus & exposure lock.
- **Full-press** (force threshold 2): capture.
- **Light-touch + slide**: parameter adjustment (zoom, EV, depth).
- **Double light-press**: cycle through parameter controls.

### API

`AVCaptureEventInteraction` (iOS 17.2+) handles the physical-button events; for the slide-and-touch refinements, use `AVCaptureControl` and conform to its hierarchy.

```swift
import AVKit

let interaction = AVCaptureEventInteraction { event in
    switch event.phase {
    case .began:
        focusAndExposureLock()
    case .ended:
        capturePhoto()
    @unknown default:
        break
    }
}
viewController.view.addInteraction(interaction)
```

### Design considerations

- **Half-press haptic is system-provided** — you don't need to fire your own.
- **Surface contextual controls during the slide gesture** — e.g., a zoom indicator that follows the slide.
- **Capture immediately on full-press release** — don't wait for the user to lift their finger entirely; capture at peak force.

This API is only relevant for camera apps. See the [Camera & Photos skill](../camera-and-photos/SKILL.md) for full camera UX coverage.

---

## 12. Symbol Effects

iOS 17 added `.symbolEffect(...)` modifiers for SF Symbols. These are the easiest free wins in iOS design.

### Built-in effects

| Effect | Use case |
| --- | --- |
| `.symbolEffect(.bounce, value: trigger)` | Confirmation of a tap, like icon pulses |
| `.symbolEffect(.pulse, options: .repeating)` | Continuous attention (recording, processing) |
| `.symbolEffect(.variableColor)` | Animated color sweep across hierarchical layers (perfect for Wi-Fi/cellular bars filling in) |
| `.symbolEffect(.scale.up)` | Emphasis on appearance |
| `.symbolEffect(.appear / .disappear)` | Tied to view visibility — animates the symbol in/out |
| `.symbolEffect(.replace, value: state)` | (iOS 17+) Morphs from one SF Symbol to another (e.g., play → pause) |
| `.contentTransition(.symbolEffect(.automatic))` | Use with `Image(systemName:)` that changes — picks the right transition |

### Concrete examples

**Send button morphs to checkmark on success:**
```swift
Image(systemName: succeeded ? "checkmark" : "paperplane.fill")
    .contentTransition(.symbolEffect(.replace))
```

**Heart pulses on like:**
```swift
Image(systemName: liked ? "heart.fill" : "heart")
    .foregroundStyle(liked ? .red : .gray)
    .symbolEffect(.bounce, value: liked)
```

**Wi-Fi loading animation:**
```swift
Image(systemName: "wifi")
    .symbolRenderingMode(.hierarchical)
    .symbolEffect(.variableColor.iterative, isActive: isLoading)
```

### Rules

- **Use sparingly.** Symbol effects everywhere = visual cacophony. Pick 3–5 moments per app.
- **Tie to user action.** A symbol that bounces on its own (no user interaction) is annoying.
- **Pair with haptics.** A bouncing heart + a `.medium` impact = perfect like-button feel. Either alone = forgettable.

---

## 13. Focus filters

iOS 16+: users can configure which content from your app appears during specific Focus modes (Work, Personal, Sleep, etc.).

### Use cases

- A messaging app hides certain group chats during Sleep focus.
- A news app shows only specific topics during Work focus.
- A music app picks a different default playlist per focus.

### Implementation

Provide a `SetFocusFilterIntent`:

```swift
import AppIntents

struct InboxFocusFilter: SetFocusFilterIntent {
    static var title: LocalizedStringResource = "Inbox Focus Filter"
    static var description: LocalizedStringResource = "Filter which inboxes appear during this Focus."

    @Parameter(title: "Selected Inboxes")
    var inboxes: [InboxEntity]

    func perform() async throws -> some IntentResult {
        await UserDefaults(suiteName: "group.com.app")?
            .set(inboxes.map(\.id), forKey: "focus.activeInboxes")
        return .result()
    }
}
```

Users see your filter in Settings → Focus → [Focus mode] → Apps. They configure the parameter, and your intent runs whenever that Focus activates.

---

## Animation curves cheat sheet (cross-surface)

| Surface | Curve | Notes |
| --- | --- | --- |
| Widget number change | `.contentTransition(.numericText())` | System-driven, just opt in |
| Symbol replace | `.contentTransition(.symbolEffect(.replace))` | iOS 17+ |
| Live Activity content change | (system-driven) | You don't animate; the system snapshots & morphs |
| Compact → Expanded DI | (system-driven) | Make snapshots structurally similar to avoid jank |
| Context menu open | (system-driven) | Use `.contextMenu` and trust it |
| Lock Screen Live Activity reveal | `.spring(response: 0.42, dampingFraction: 0.85)` | System default — match it in your in-app transitions |
| Haptic Touch lift | `.spring(response: 0.32, dampingFraction: 0.75)` | When implementing custom menus |
| Action Button feedback | n/a | Use audio + haptic, NOT visual (button is on the side) |
| Control Widget toggle | (system-driven) | Just provide on/off states |

---

## Haptics cheat sheet (cross-surface)

| Surface | Haptic |
| --- | --- |
| Widget Button tap | The system fires a default selection haptic — don't double-fire from your intent |
| Widget Toggle change | Same — system handles it |
| Live Activity tap (opens app) | System haptic on transition |
| Dynamic Island long-press to expand | System-provided, you don't add to it |
| Context menu open | System fires `.medium` |
| Context menu item select | System fires `.medium` |
| Context menu dismiss (outside) | System fires `.soft` |
| Action Button trigger | NONE from the OS — YOU should fire `.success` notification haptic in your intent's `perform()` |
| Camera Control half-press | System provides distinctive "click" haptic |
| Camera Control full-press | System provides — pair with shutter haptic in your camera app |

Rule: **don't double-fire**. If the system fires, don't add yours. If the system is silent (Action Button), YOU must fire.

---

## iOS 26 Liquid Glass considerations

iOS 26 (released September 2025) introduces the Liquid Glass material across the system. For peripheral surfaces:

- **Widgets** automatically pick up Liquid Glass when you use `.containerBackground(.fill.tertiary, for: .widget)`.
- **Use `.widgetAccentable()`** on elements that should tint under the user's accent rendering mode.
- **Live Activities** render with Liquid Glass on the Lock Screen — no API change needed.
- **Dynamic Island** is unaffected (it's already a "canvas of foreground elements").
- **Control Center widgets** inherit Liquid Glass automatically.

You don't need to opt in to Liquid Glass for most surfaces — just stop hardcoding background colors. Use semantic system fills (`.fill.tertiary`, `.fill.quaternary`) and let the system render the material.

For app-side UI on iOS 26, the `glassEffect()` modifier (or `expo-glass-effect` for Expo apps) gives you Liquid Glass on custom views. Don't apply it to widgets — they use the system widget container, which already handles it.

---

## Anti-patterns to avoid (the full list)

1. **Widgets that update too often.** You'll burn through the system budget and the user will see stale content. Update only when there's meaningful change.
2. **Live Activities that don't end.** A 6-hour-old "Pizza is on the way" activity is a worse UX than no activity. Set `staleDate`. End within reason.
3. **Dynamic Island backgrounds.** Apple's HIG is explicit. Foreground elements only.
4. **Interactive buttons in compact/minimal DI presentations.** Apple's HIG forbids them. Use expanded only.
5. **Haptics on every interaction.** Vibrating phone. Pick the 5–10 moments per app where haptics genuinely add value.
6. **Symbol effects on every icon.** Visual noise. Pick 3–5 moments.
7. **Context menus as the only path to an action.** Discoverability hell. Mirror in visible UI.
8. **Cold-calling the haptic engine.** Always `prepare()` first. Always reuse generator instances.
9. **Tying the same App Intent to "open the app" + "perform action".** Decide which one this is and commit.
10. **Adding a logo to your widget.** The app icon IS the logo, shown beside the widget by the system. Don't duplicate.
11. **Lock Screen widgets in full color.** Apple's HIG quietly discourages this; the tint-mode is the iOS aesthetic.
12. **A Live Activity that announces "X started" then "X finished" with no updates in between.** That's a notification, not a Live Activity.
13. **Custom haptic patterns longer than 30 seconds.** API limit. And way too long anyway.
14. **Forgetting to test in red-tint StandBy mode.** Most apps fail this test.

---

## Permission & privacy

- Live Activities require user consent: the user must enable "Live Activities" for your app in Settings (default on).
- Push tokens for Live Activities are NOT the same as your APNs device token — request a new one per activity.
- Widget data MUST be stored in an App Group container if both your app and the widget extension need to read it. Use `UserDefaults(suiteName: "group.com.app")`.
- Sensitive data on Lock Screen widgets: use `.privacySensitive(true)` to redact when the device is locked. Currently mostly honored by Apple Watch faces, but use it everywhere for future-proofing.

---

## Implementation checklist for a new app

Use this when adding peripheral surfaces:

### Widgets
- [ ] **Define App Intents** for the 1–3 core actions (toggle, log, navigate).
- [ ] **Home widget**: `.systemSmall` + `.systemMedium` minimum. `.systemLarge` if list-based.
- [ ] **Lock Screen widget**: `.accessoryCircular` + `.accessoryRectangular`.
- [ ] **StandBy support**: confirm `.systemSmall` looks great at 6 feet, including red-tint mode.
- [ ] **iOS 26 Liquid Glass**: use semantic backgrounds, `.widgetAccentable()` where appropriate.
- [ ] **Refresh policy**: long timelines with `.after(longInterval)` policy.
- [ ] **App Group**: shared container for widget ↔ app data.

### Live Activities
- [ ] **`ActivityAttributes`** defined with stable identity + dynamic `ContentState`.
- [ ] **Lock Screen presentation** with route/map/progress hero.
- [ ] **Dynamic Island compact** + **expanded** + **minimal** presentations.
- [ ] **`staleDate`** set on every update.
- [ ] **`pushTokenUpdates`** observer → server.
- [ ] **End policy**: `.after(now + 60)` for "completed" states.
- [ ] **Test**: minimal mode (start 2 activities at once), expanded mode (long-press in simulator).

### Control Center widget (iOS 18+)
- [ ] **ControlWidget** declared.
- [ ] **`ControlWidgetButton` or `ControlWidgetToggle`** with associated AppIntent.
- [ ] **Custom SF Symbol** in asset catalog (if not using stock).

### Haptics
- [ ] **Audit every tappable element** — does it haptic?
- [ ] **`UIFeedbackGenerator` instances** are class properties (reused), not locals.
- [ ] **`prepare()`** in `viewDidAppear` / `.onAppear`.
- [ ] **CoreHaptics engine** wrapped in a singleton.
- [ ] **At least one custom AHAP pattern** for the app's signature moment.
- [ ] **Test on a real device** — simulator has no haptics.

### Action Button & Camera Control
- [ ] **AppShortcutsProvider** with 1–3 phrases.
- [ ] **AppIntent**(s) with `openAppWhenRun = false`.
- [ ] **Success haptic** fires from the intent's `perform()`.
- [ ] **Long actions**: kick off Live Activity for confirmation.

### Context menus
- [ ] **Every list cell** has a context menu with 3–5 relevant actions.
- [ ] **Preview** included for photos/cards.
- [ ] **Destructive actions** marked `role: .destructive`.
- [ ] **Mirror context-menu actions** in a visible UI (swipe, button, etc.).

### Symbol Effects (iOS 17+)
- [ ] **Like/save/favorite icons** use `.bounce` with `value:`.
- [ ] **Play ↔ Pause toggles** use `.replace`.
- [ ] **Loading indicators** use `.variableColor` or `.pulse`.

---

## Final principles

1. **Peripheral surfaces are the product for most users most of the time.** A widget seen 100× a day matters more than a screen seen 5×.
2. **One App Intent. Many surfaces. No duplicated logic.** Architect around intents from day one.
3. **The Dynamic Island is a stage, not a billboard.** Less is more. Always.
4. **Haptics are punctuation.** A `.` not a `!`.
5. **The half-second test**: if a user can't parse your widget / Live Activity / Dynamic Island in 0.5 seconds, it's broken. Redesign.
6. **Glanceability over completeness.** Show the ONE thing that matters. The app is for the rest.
7. **Default everything correctly.** Most users don't customize. Make the out-of-box experience the polished one.

The benchmark: a user puts their phone face-down on the table. Six hours later, they glance at it. Your Lock Screen widget tells them what they need in under a second. They don't open your app — because they didn't need to. THAT is when you've won.


---

## The Final 5% — iOS Polish

_When to use this section: The final 5% of detail that separates a competent iOS app from a beloved one. Use this skill whenever the user is building, reviewing, or polishing a native Swift/SwiftUI iOS app and wants it to feel custom, considered, and crafted — like Halide, Things 3, Linear, Granola, or Apple's own apps. Triggers on: polish, premium feel, details, micro-interactions, craft, attention to detail, taste, feels generic, doesn't feel right, missing something, make it premium, make it feel custom, animation polish, transitions, hero animation, matchedGeometryEffect, spring animations, easing curves, .smooth, .snappy, .bouncy, content transitions, numeric text, symbol effects, SF Symbols, SF Pro typography, optical sizes, dynamic type, tracking, kerning, line height, color hierarchy, semantic colors, true black, OLED, Liquid Glass, iOS 26 design, glass effect, glassEffect, GlassEffectContainer, sensoryFeedback, haptic feedback patterns, sound design, empty states, loading states, skeleton screens, blurhash, image fade in, hero transitions, celebrations, confetti, onboarding polish, paywall polish, settings polish, microcopy, voice, tone, accessibility as polish, Reduce Motion, Dynamic Type, VoiceOver, tap target, .contentShape, interruptible animations, rubber banding, parallax, drag interactions, page transitions, modal presentation, sheet detents._

# The Final 5% — iOS Design Engineering Skill

> "Whoever made this actually gives a shit."

That's the only goal. Everything in this file is in service of someone using your app and feeling, in their bones, that a human cared. This is the skill you load when the app *works* but doesn't *feel right*. When everything compiles and ships but the spark is missing.

This skill assumes a native Swift/SwiftUI iOS app, targeting iOS 17 minimum and ideally iOS 26 (Liquid Glass). It pairs with [camera-and-photos](../camera-and-photos/SKILL.md), [chat-and-messaging](../chat-and-messaging/SKILL.md), and [interaction-primitives](../interaction-primitives/SKILL.md) — but the patterns here apply to every app.

---

## Philosophy

The principle these apps share — Halide, Kino, Things 3, Linear, Family, Granola, Apple's first-party apps:

> **They didn't make an app. They made the thing.**

Halide's team said it explicitly: *"We didn't make an app — we made a camera."* They commissioned a custom typeface (Halide Router) inspired by Leica lens engravings. Things 3 makes to-dos look like plain text until you touch them, when boundaries materialize. Linear started with quality and *then* learned that people noticed. Granola talks about "invisible design" — polish so deep it disappears.

These products share three properties:
1. **Conviction.** Every detail is opinionated. There is one right way to do this, and the team picked it.
2. **Restraint.** The polish doesn't shout. A heart icon that pulses on tap with a 0.18s spring + a soft haptic is not a feature to brag about in the changelog — it's just *what a like button should be*.
3. **Coherence.** Every surface feels related — the loading state, the empty state, the settings, the paywall, the celebration. The error screen has the same care as the hero. The "dirty bathroom" rule: one neglected corner cheapens the whole.

Three pillars that govern everything below (adapted from Family's [design-with-taste](https://family.co) philosophy for native iOS):

### 1. Gradual revelation
Show only what matters *right now*. Each touch unfolds the next layer. The interface is rooms, not a menu. Apple Photos doesn't show every album the moment you open it — it shows Library. iMessage doesn't show every reaction on screen — long-press to reveal. Tap → reveal → repeat.

### 2. Spatial fluidity
Treat the app as a place with physical rules. Every element has a *from* and a *to*. Nothing teleports. A card that opens to a detail view doesn't unmount and remount — it morphs via `matchedGeometryEffect`. A chevron flips when you tap to reveal. The composer pill grows into a bubble that flies to its slot. The app is one continuous space, not a slideshow.

### 3. Selective delight
The Delight-Impact Curve: rare interactions deserve theatrical moments; frequent ones deserve subtle ones. A like button gets a haptic + a soft scale. A first-time milestone gets confetti. Both are correct. What's *wrong* is the inversion: confetti on every save, silence on a milestone.

---

## Section index

| Section | Topic |
| --- | --- |
| [§1](#1-motion) | Motion — springs, easing, timing |
| [§2](#2-hero-transitions--matchedgeometryeffect) | Hero transitions & matchedGeometryEffect |
| [§3](#3-content-transitions) | Content transitions (numericText, symbolEffect, interpolate) |
| [§4](#4-typography) | Typography — SF Pro family, optical sizes, tracking, Dynamic Type |
| [§5](#5-color--material) | Color & material — OLED black, semantic hierarchy, Liquid Glass |
| [§6](#6-spacing-rhythm--optical-alignment) | Spacing, rhythm & optical alignment |
| [§7](#7-sf-symbols--symbol-effects) | SF Symbols & Symbol Effects |
| [§8](#8-haptics--sensoryfeedback) | Haptics — `.sensoryFeedback` and CoreHaptics combos |
| [§9](#9-sound-design) | Sound design — when, what, how loud |
| [§10](#10-touch--gesture-polish) | Touch & gesture polish |
| [§11](#11-image--media-polish) | Image & media polish — fade-in, blurhash, vignettes |
| [§12](#12-loading-states) | Loading states — skeletons, shimmers, optimistic UI |
| [§13](#13-empty-states) | Empty states — first impressions |
| [§14](#14-celebrating-completions) | Celebrating completions — confetti theory |
| [§15](#15-onboarding-polish) | Onboarding polish |
| [§16](#16-paywall-polish) | Paywall polish |
| [§17](#17-settings-polish) | Settings polish |
| [§18](#18-microcopy--voice) | Microcopy & voice |
| [§19](#19-accessibility-is-polish) | Accessibility is polish — Reduce Motion, Dynamic Type, VoiceOver storytelling |
| [§20](#20-liquid-glass-ios-26) | Liquid Glass — iOS 26 |
| [§21](#21-the-final-5-checklist) | The Final 5% checklist |
| [§22](#22-anti-patterns) | Anti-patterns |

---

## 1. Motion

Motion is the personality of your app. It's the difference between "this works" and "this feels alive."

### The two spring APIs to know

**iOS 17+ duration/bounce springs (preferred):**
```swift
.animation(.spring(duration: 0.42, bounce: 0.22), value: state)
```
- `duration`: perceived time to settle. 0.18–0.5s for most UI.
- `bounce`: 0 = critically damped (no overshoot), 0.3+ = noticeably bouncy. Most UI: 0.15–0.25.

**Three named presets** (iOS 17+):
- `.smooth` — critically damped, no overshoot. Use for serious/important transitions (push nav, sheet present).
- `.snappy` — slight overshoot, fast settle. Use for tap responses, toggles, filter chips.
- `.bouncy` — pronounced overshoot. Use for playful moments: confetti, sticker drops, celebration.

```swift
withAnimation(.smooth(duration: 0.4)) { showDetail = true }       // serious
withAnimation(.snappy(duration: 0.28, extraBounce: 0.1)) { ... } // tap response
withAnimation(.bouncy(duration: 0.5, extraBounce: 0.2)) { ... }  // playful
```

### The motion cheat sheet for iOS

| Surface | Spring | Notes |
| --- | --- | --- |
| Button press (scale down on touch) | `.spring(duration: 0.16, bounce: 0)` | Fast. Match by scaling to 0.97 |
| Button release | `.spring(duration: 0.3, bounce: 0.25)` | Bouncier than press — feels satisfying |
| Tab selection indicator | `.snappy(duration: 0.28, extraBounce: 0.12)` | Crisp |
| Filter chip select | `.snappy(duration: 0.24)` | |
| Modal sheet present | `.spring(duration: 0.42, bounce: 0.18)` | Standard iOS feel |
| Sheet dismiss | `.spring(duration: 0.32, bounce: 0)` | Faster than present, no bounce |
| Hero transition (`matchedGeometryEffect`) | `.spring(duration: 0.42, bounce: 0.16)` | iOS-native |
| Push navigation | system default | Don't override |
| Page indicator (paging) | `.spring(duration: 0.32, bounce: 0.15)` | |
| Drawer open | `.spring(duration: 0.36, bounce: 0.18)` | |
| Drawer close (drag-dismiss with velocity) | `.interpolatingSpring(stiffness: 350, damping: 32, initialVelocity: gestureVelocity)` | Velocity-aware |
| Slider thumb | `.linear` ONLY | Springs fight the finger |
| Crop dial | `.linear` | Same |
| Toggle thumb | `.snappy(duration: 0.24, extraBounce: 0.2)` | Subtle bounce on flip |
| Card lift (long-press) | `.spring(duration: 0.32, bounce: 0.18)` | |
| Hover preview (haptic-touch) | `.spring(duration: 0.32, bounce: 0)` | No overshoot — feels precise |
| Reaction picker emoji stagger | `.snappy(duration: 0.32, extraBounce: 0.25)` + 0.04s delay each | |
| Confetti / celebration | `.bouncy(duration: 0.6, extraBounce: 0.3)` | |
| Skeleton shimmer cycle | `.linear(duration: 1.2).repeatForever()` | Linear is correct here — perpetual motion |

### Easing curves (for non-spring animations)

Springs cover ~90% of cases. For the rest:

| Curve | Swift | When |
| --- | --- | --- |
| `.easeOut` | `.easeOut(duration: 0.24)` | Entering elements, color changes, ambient transitions |
| `.easeIn` | `.easeIn(duration: 0.18)` | Exiting elements |
| `.easeInOut` | `.easeInOut(duration: 0.32)` | Continuous position changes (scroll, pan) |
| `.linear` | `.linear(duration: 0.2)` | Indeterminate loaders, shimmer, follow-finger gestures |
| Custom | `.timingCurve(0.16, 1, 0.3, 1, duration: 0.4)` | Family's golden curve — fast start, gentle settle |

**Never use `.easeIn` on entering elements.** It looks like the app is reluctant.

### Stagger — the most important polish trick

> "Simultaneous motion reads as mechanical. Sequential motion reads as organic." — Rauno Freiberg

When several elements animate at once, delay each by 30–80ms. This single trick is the difference between feeling like software and feeling like a thing.

```swift
// Bad — all dots animate together; looks mechanical
ForEach(0..<5) { i in
    Circle()
        .scaleEffect(animating ? 1.0 : 0.0)
        .animation(.spring(duration: 0.4), value: animating)
}

// Good — staggered, reads as a wave
ForEach(0..<5) { i in
    Circle()
        .scaleEffect(animating ? 1.0 : 0.0)
        .animation(.spring(duration: 0.4).delay(Double(i) * 0.05), value: animating)
}
```

For lists, cells should fade/slide in with stagger when first appearing — but ONLY on first appearance, not on every scroll into view (that's exhausting).

### Unified interpolation — the "one breathing unit" rule

Stagger is for *independent* elements arriving together. **Unified interpolation** is for *dependent* elements representing one underlying value. They're different problems with different solutions, and getting them confused is a common amateur tell.

When multiple visual elements are driven by the same data — a chart line, its value label, an axis tick, and a status badge all tied to the same number — they must share the SAME easing and duration. If the line uses `.spring(duration: 0.4, bounce: 0.18)` but the label uses `.linear(duration: 0.2)`, the eye picks up the disagreement and the interface reads as a collection of widgets instead of one thing breathing.

```swift
// Bad — line and label fight each other
chartLine.animation(.spring(duration: 0.42, bounce: 0.18), value: value)
valueLabel.animation(.linear(duration: 0.2), value: value)

// Good — one source of truth
let valueAnim: Animation = .spring(duration: 0.42, bounce: 0.18)
chartLine.animation(valueAnim, value: value)
valueLabel.animation(valueAnim, value: value)
axisTick.animation(valueAnim, value: value)
statusBadge.animation(valueAnim, value: value)
```

When a balance updates: the number rolls, the bar grows, the indicator dot moves — all on one breath. That's what "alive" feels like.

### Interruptible animations

The hallmark of professional motion: animations you can interrupt mid-flight by touching them again.

In SwiftUI, this is mostly automatic — if you wrap your state change in `withAnimation`, a new state change mid-animation will smoothly re-target from the current position. Don't fight this with `.animation(value:)` modifiers in the wrong place.

For gesture-driven animations, use `interpolatingSpring(initialVelocity:)` and pass the gesture's predicted velocity:

```swift
.gesture(
    DragGesture()
        .onEnded { value in
            let velocity = value.predictedEndLocation.y - value.location.y
            withAnimation(.interpolatingSpring(
                stiffness: 320,
                damping: 28,
                initialVelocity: velocity / 100
            )) {
                offset = .zero
            }
        }
)
```

The velocity carry-through is what makes physics-based UI feel real.

### Don't animate everything

A list scrolling 60fps doesn't need animations on cells. A status pill that updates with new server data doesn't need a spring — instant change is fine. **Animate user-initiated changes. Let data changes happen.** The exception: numeric values changing (see §3).

### Always scope `.animation(_, value:)` to specific state

The single most common SwiftUI motion bug: a blanket `.animation(.snappy)` modifier that animates EVERY state change — including ones you didn't intend. Always pair `.animation(...)` with `value:`:

```swift
// Bad — animates on EVERY state change, including unrelated re-renders
view.animation(.snappy)

// Good — animates only when isExpanded changes
view.animation(.snappy, value: isExpanded)
```

This is the iOS equivalent of the web's "never use `transition: all`" rule. Specify exactly what triggers the animation. When you want different animations on different state changes, chain them:

```swift
view
    .animation(.snappy(duration: 0.24), value: isExpanded)
    .animation(.smooth(duration: 0.4), value: contentChanged)
```

Adopting this discipline early prevents 90% of "why is this animating?" debugging sessions later.

---

## 2. Hero transitions & matchedGeometryEffect

The single most important polish technique in modern SwiftUI. A card that "flies" into its detail view is the iOS-native feel. Done right, the user's brain doesn't process it as a transition — it processes it as picking up an object.

### The pattern

```swift
@Namespace private var heroNamespace
@State private var expandedID: UUID?

ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemCard(item: item)
                .matchedGeometryEffect(id: item.id, in: heroNamespace)
                .onTapGesture {
                    withAnimation(.spring(duration: 0.42, bounce: 0.16)) {
                        expandedID = item.id
                    }
                }
        }
    }
}
.overlay {
    if let id = expandedID,
       let item = items.first(where: { $0.id == id }) {
        ItemDetail(item: item)
            .matchedGeometryEffect(id: id, in: heroNamespace)
            .onTapGesture {
                withAnimation(.spring(duration: 0.42, bounce: 0.16)) {
                    expandedID = nil
                }
            }
    }
}
```

### The details that separate amateur from amazing

1. **The DESTINATION view must structurally resemble the source.** If your card has rounded corners (18pt), an image at the top, and text below — the detail view must START with that exact layout, then expand outward as the animation plays. Don't morph an 18pt corner directly into a sharp edge — animate corner radius from 18 → 0 over the same duration.

2. **Match the corner radius transition.** Use `.containerRelativeShape()` or animate the corner radius explicitly. Sharp corners on a phone aspect-ratio detail view need `cornerRadius` going from 18 → 38 (iPhone bezel) → 0 over the animation.

3. **The non-hero elements stagger in.** Once the hero element has landed (say at 0.3s into a 0.42s spring), other elements on the detail page (description, buttons, related items) fade/slide in with a stagger of 40–60ms each, starting at ~0.3s after the hero begins.

```swift
struct DetailView: View {
    let item: Item
    @State private var bodyVisible = false

    var body: some View {
        VStack(spacing: 0) {
            // Hero — matched
            ItemHero(item: item)
                .matchedGeometryEffect(id: item.id, in: namespace)

            // Body — staggered fade-in after hero lands
            VStack(spacing: 16) {
                Text(item.title)
                Text(item.body)
                ActionButton()
            }
            .opacity(bodyVisible ? 1 : 0)
            .offset(y: bodyVisible ? 0 : 12)
            .animation(.spring(duration: 0.5, bounce: 0.15).delay(0.18), value: bodyVisible)
            .onAppear { bodyVisible = true }
        }
    }
}
```

4. **Status bar handling.** When the hero expands to fill the screen, the status bar tint should transition from light/dark based on the new background. Use `.statusBarHidden()` or `.toolbarColorScheme(.dark, for: .navigationBar)` to coordinate.

5. **Drag-to-dismiss.** Once expanded, dragging down should rubber-band the hero back to its source. Use `.gesture(DragGesture())` with progressively decreasing scale and corner radius as the drag grows. Release past 120pt OR with velocity > 600pt/s dismisses.

6. **The reverse animation should be SHORTER than the open animation.** Open: 0.42s. Close: 0.32s. People want OUT faster than they want IN.

### Persistent elements never animate out and back in

If a nav title, status pill, or chrome element exists in BOTH the source and the destination of a transition, it must stay put. Don't fade it out with the source and re-fade it in with the destination — that's the most common amateur transition mistake. The element either morphs in place via `matchedGeometryEffect` (if its position changes) or simply remains rendered (if its position is fixed).

```swift
// Bad — title fades out with source, fades back in with destination
ZStack {
    if showingDetail {
        DetailView() // mounts a fresh "Inbox" title that fades in
    } else {
        ListView()   // contains "Inbox" title that fades out
    }
}

// Good — title persists in a parent that survives the transition
VStack {
    Text("Inbox").matchedGeometryEffect(id: "title", in: ns)
    Group {
        if showingDetail { DetailView() } else { ListView() }
    }
}
```

The rule: before designing any transition, ask which elements *should* survive. Render those in a parent that survives. Animate only what's actually changing. Anything redundantly animating in and out is noise.

### Reference apps

- **Apple App Store** — the gold standard. Tap any "Today" tile and watch.
- **Apple Photos** — tap a photo, watch the hero. The thumb and full-size image are matched.
- **Things 3** — to-dos expand into edit mode. Watch closely: the existing text stays put, the chrome (input field background, action buttons) materializes around it.

### Mobbin references

- [Shangri-La Circle — article detail](https://mobbin.com/flows/76798415-4dce-47b8-befc-659a5fea7ff6) — hero card → article with sticky chrome
- [Skillshare — project details](https://mobbin.com/flows/155af18f-a4ba-4443-91f7-318c9238c052) — illustration hero with staggered metadata
- [Moonlitt — tradition detail](https://mobbin.com/flows/78295e9d-f782-42e5-83d8-1c13c2991f5d) — dark theme, paginated detail

---

## 3. Content transitions

When TEXT changes, it should not pop. iOS has dedicated APIs for this since iOS 16.

### `.contentTransition(.numericText())`

For changing numbers — counters, prices, scores, durations, timers. Digits *roll* like an odometer.

```swift
Text("\(score)")
    .font(.system(size: 48, weight: .bold, design: .rounded))
    .contentTransition(.numericText(value: Double(score)))
    .animation(.snappy(duration: 0.3), value: score)
```

**Critical**: also apply `.monospacedDigit()` (or use SF Mono, or SF Pro Rounded with `.monospacedDigit()` modifier) for changing numbers, OR the layout will SHIFT as digit widths vary. Tabular numerals is a separate requirement — `.numericText()` doesn't fix the layout shift on its own.

```swift
Text(score, format: .number)
    .font(.system(size: 48, weight: .bold, design: .rounded).monospacedDigit())
    .contentTransition(.numericText(value: Double(score)))
```

For countdowns: use `.numericText(countsDown: true)` — the digits roll in the OTHER direction (visually descending).

### `.contentTransition(.symbolEffect)`

For changing SF Symbols — the heart that fills, the star that gains points, the bell that rings.

```swift
Image(systemName: liked ? "heart.fill" : "heart")
    .foregroundStyle(liked ? .red : .gray)
    .contentTransition(.symbolEffect(.replace))
    .animation(.snappy, value: liked)
```

`.replace` morphs one symbol into another with a satisfying scale + opacity sequence. iOS 18+ also offers `.replace.upUp`, `.replace.downUp` etc. for directional morphs.

### `.contentTransition(.interpolate)`

For numbers, sizes, or AttributedString changes that *can* interpolate. Less common, but for cases like a fixed-position counter that just needs to crossfade with a soft hint of motion, this is the lightest option.

### `.contentTransition(.identity)`

Use when you EXPLICITLY want NO transition. Useful inside a `withAnimation` block where you want some children to skip the transition.

### Text morphing across labels

For button labels that change ("Continue" → "Confirm" → "Sending..."), SwiftUI has no built-in shared-letter morphing the way the web's `torph` does. Two iOS-native options:

**Option A — crossfade with `.transition(.opacity)`:**
```swift
ZStack {
    if state == .ready { Text("Continue") }
    if state == .confirming { Text("Confirm") }
    if state == .sending { Text("Sending...") }
}
.transition(.opacity.combined(with: .scale(scale: 0.92)))
.animation(.snappy(duration: 0.28), value: state)
```

**Option B — animatable AttributedString (iOS 17+):**
This is more involved but yields true character-level morphing. Wrap your label in a custom `AnimatableModifier` that interpolates AttributedString attributes. Worth it for hero buttons.

**Option C — third-party.** Libraries like `swift-text-morph` exist. For a standard iOS app, Option A is the right call.

### When text changes only partially

If the visible text is "Available • 3 in stock" and changes to "Available • 1 in stock", DON'T animate the entire string. Split into multiple `Text` views and only animate the changing piece.

```swift
HStack(spacing: 4) {
    Text("Available •").foregroundStyle(.green)
    Text("\(count) in stock")
        .contentTransition(.numericText(value: Double(count)))
        .animation(.snappy, value: count)
}
```

---

## 4. Typography

Typography is the single highest-leverage area for "premium feel". Get this right and everything else looks more considered.

### SF Pro — know your family

| Variant | Sizes | When |
| --- | --- | --- |
| `SF Pro Text` | < 20pt | Body text, captions, metadata. Tracking is opened up automatically; letters are wider. |
| `SF Pro Display` | ≥ 20pt | Large titles, hero numbers. Tighter tracking; tighter letterforms. |
| `SF Pro Rounded` | any | Friendly, organic. Great for numeric displays, kids/health/wellness apps, large hero numerals. |
| `SF Mono` | any | Code, changing numbers (ticker, timer), monospace columns. |
| `SF Compact` | any | iPhone-only (NOT Mac/iPad). Slightly narrower; saves horizontal space. |

**iOS does the optical-size swap automatically.** When you use `.font(.system(size: 13))`, you get SF Pro Text. When you use `.font(.system(size: 34))`, you get SF Pro Display. **Don't fight this.**

### The system Dynamic Type styles (always prefer these)

Hard-coded sizes are a polish anti-pattern. Use semantic styles:

| SwiftUI | Default size | Use case |
| --- | --- | --- |
| `.largeTitle` | 34pt | Large nav titles |
| `.title` | 28pt | Section heroes |
| `.title2` | 22pt | Subsection titles |
| `.title3` | 20pt | Smaller hero |
| `.headline` | 17pt semibold | Card titles, cell titles |
| `.body` | 17pt | Body text. The default. |
| `.callout` | 16pt | Slightly smaller body |
| `.subheadline` | 15pt | Cell subtitles |
| `.footnote` | 13pt | Small captions, hints |
| `.caption` | 12pt | Smallest |
| `.caption2` | 11pt | Smaller smallest |

```swift
Text("Welcome back")
    .font(.title.weight(.semibold)) // gets Dynamic Type for free
```

**Apply weights via `.weight()` after `.font(...)`,** so Dynamic Type still works.

### Tracking — let SF Pro do it

SF Pro has a built-in tracking table — automatic letter-spacing per point size. **Don't override it.** Adding `.tracking()` to system text undoes Apple's careful work.

**Exceptions** (when manual tracking is appropriate):
- All-caps labels — Apple itself adds positive tracking (~1.2–2.0pt) for caps.
- Numeric displays where you want monospace digit columns — use `.monospacedDigit()` modifier instead of tracking.
- Display sizes 60pt+ where you want negative tracking for tighter visual: `-0.5` to `-1.5`.

```swift
Text("AE/AF LOCK")
    .font(.system(size: 11, weight: .heavy))
    .tracking(1.8)
    .textCase(.uppercase)
```

### Line height

For body text: 1.4× font size is the standard reading rhythm.
For display text (28pt+): 1.1–1.2× — tighter, more impactful.
For headlines: 1.15×.

In SwiftUI, control with `.lineSpacing(...)` (which adds to the natural line height) or with `.font(.body.leading(.tight | .loose | .standard))`.

### The five typography mistakes that signal "amateur"

1. **Using `.regular` for everything.** Mix `.regular` and `.semibold`. Hierarchy.
2. **Same size everywhere.** A 17pt body next to a 17pt headline = no hierarchy. Use 17pt + 22pt + 28pt as your spine.
3. **Light weights under 20pt.** SF Pro Light at small sizes is illegible. Reserve light weights for large hero text only.
4. **Center-aligning body text.** Looks like a marketing landing page. Body text should be left-aligned (or `.leading` for RTL support).
5. **Custom fonts for body.** If you're going to use a custom font, use it for hero numerals or section titles — never for body. SF Pro is unmatched for legibility on iOS.

### Custom fonts done right

If you DO use a custom font (and you can — Halide's Router proves it's worth it), follow these rules:
- **Pair it with SF Pro** for body. Custom for display, system for reading.
- **Test on the smallest reading size** — at 13pt, most custom fonts are unreadable.
- **Register via `UIFont.registerFont`** in `application(_:didFinishLaunchingWithOptions:)` so it's available app-wide.
- **Match weights**. If your custom font has only Regular and Bold, but Apple's HIG calls for semibold, add a Medium or use `kCTFontWeightTrait` to interpolate.

### Numbers — the secret weapon

For any UI showing numbers that change:
```swift
.font(.system(size: 36, weight: .bold, design: .rounded).monospacedDigit())
```

`.monospacedDigit()` keeps digits the same width, so a number rolling from 99 → 100 doesn't shift the layout. Critical for: counters, scores, timers, prices, statistics, fitness data.

For numbers that should feel friendly: `design: .rounded`. For numbers that should feel precise: `design: .default` (SF Pro).

### Smart formatting

Use Apple's formatters — don't hand-roll:
```swift
// Currency
price.formatted(.currency(code: "USD"))

// Compact numbers (1.2K instead of 1,234)
count.formatted(.number.notation(.compactName))

// Relative dates (2 minutes ago, yesterday)
Text(date, style: .relative)
Text(date.formatted(.relative(presentation: .named)))

// Distance with locale-aware units
distance.formatted(.measurement(width: .abbreviated, usage: .road))
```

Localization, accessibility, and visual polish all improve when you use these.

---

## 5. Color & material

### True black for OLED

On OLED displays (every iPhone since X), `#000000` literally turns OFF the pixel. This means:
- True black backgrounds have ZERO battery cost.
- True black has perfect contrast — no light bleed between elements.
- True black backgrounds make photos look 10× better (they appear self-illuminated).

**Use true black for**:
- Camera viewfinder chrome backgrounds
- Photo viewer backgrounds
- Cinematic media UIs (video player, podcast)
- App backgrounds for media-first apps in dark mode

**Don't use true black for**:
- Reading/text-heavy interfaces — too high-contrast, causes eye strain. Use `Color(.systemBackground)` which is `#000` only in dark mode and adjusts.
- Settings, lists, forms — `.systemGroupedBackground` is more appropriate.

```swift
// Camera viewfinder
.background(Color.black) // true #000

// Reading app
.background(Color(.systemBackground)) // adaptive
```

### Semantic colors — always use them

Hard-coded colors are a polish anti-pattern. Use Apple's semantic system colors so your app adapts to light/dark mode, increased contrast, and accent color overrides automatically.

| Token | Light | Dark | Use |
| --- | --- | --- | --- |
| `.primary` | black | white | Body text |
| `.secondary` | gray 60% | gray 60% | Secondary text |
| `Color(.label)` | black | white | Same as `.primary` but UIKit-style |
| `Color(.secondaryLabel)` | gray 60% | gray 60% | |
| `Color(.tertiaryLabel)` | gray 30% | gray 30% | Less important info |
| `Color(.quaternaryLabel)` | gray 18% | gray 18% | Placeholder, hints |
| `Color(.systemBackground)` | white | black | Main background |
| `Color(.secondarySystemBackground)` | gray 96% | gray 14% | Card surfaces |
| `Color(.tertiarySystemBackground)` | white | gray 22% | Inset cards |
| `Color(.systemGroupedBackground)` | gray 95% | true black | Settings list bg |
| `Color(.separator)` | gray 80% / 30% opacity | gray 25% / 30% opacity | Hairlines |

For accent: `.tint(...)` propagates an accent color to all interactive elements (`Button`, `Toggle`, etc.). Set it once at the root.

### Color hierarchy — 4 levels

Apple uses 4 levels of foreground opacity to express hierarchy:
- **Primary** (100%) — body, titles
- **Secondary** (60%) — subtitles, captions, less important
- **Tertiary** (30%) — placeholders, hints
- **Quaternary** (18%) — disabled, ghost

```swift
Text("Title").foregroundStyle(.primary)
Text("Subtitle").foregroundStyle(.secondary)
Text("Caption").foregroundStyle(.tertiary)
```

Use these instead of `.opacity(0.6)`. They adapt to Increased Contrast mode automatically.

### The accent rule

**Tint ONE THING per screen.** Linear's CEO Karri Saarinen says it directly: if you're an opinionated product, you commit to opinions. Tinting every interactive element makes the screen scream. Tint the PRIMARY action only.

If your tint is blue, tinted buttons are blue, but secondary buttons are gray/neutral. Tertiary actions are text-only.

### Shadows

Native iOS doesn't shadow much — Material Design loves shadows, iOS loves blur and depth. When you do need a shadow:
- **Subtle**: `.shadow(color: .black.opacity(0.06), radius: 8, x: 0, y: 4)`
- **Card lift**: `.shadow(color: .black.opacity(0.12), radius: 16, x: 0, y: 8)`
- **Floating element**: `.shadow(color: .black.opacity(0.18), radius: 24, x: 0, y: 12)`

**Never use pure black shadows.** Use `.black.opacity(0.05–0.2)` or tint the shadow with the element's color (a blue button → `.blue.opacity(0.2)` shadow). Real-world shadows pick up the color of the object.

In dark mode, shadows should be LIGHTER, not darker — you're already on a dark background. Often skip them entirely; use a 1pt stroke at `Color.white.opacity(0.06)` for separation instead.

### Materials (blur backgrounds)

For floating overlays, modals, sticky chrome: use SwiftUI's built-in materials:

| Material | Use |
| --- | --- |
| `.ultraThinMaterial` | Very translucent — see-through blur |
| `.thinMaterial` | Translucent |
| `.regularMaterial` | Standard frosted glass |
| `.thickMaterial` | Heavily blurred but still translucent |
| `.ultraThickMaterial` | Almost opaque |

```swift
HStack { ... }
    .padding()
    .background(.thinMaterial, in: RoundedRectangle(cornerRadius: 18, style: .continuous))
```

These adapt to light/dark automatically. On iOS 26, they coordinate with Liquid Glass (see §20).

### Gradient discipline

Gradients are a polish minefield. The wrong gradient screams "AI-generated app".

**Rules:**
- Use 2-stop gradients at most. 3+ stops = chaos unless you're showing a sunset.
- Use HSL/HCT interpolation, NOT RGB. SwiftUI uses RGB by default; use `Gradient(colors:)` with carefully-chosen intermediate stops to fake HSL interpolation.
- Avoid the AI gradient cliché: purple → blue → pink. If your app needs a hero gradient, use brand colors only or pick from premium palettes (warm earth tones, monochrome with a single accent).
- For backgrounds, prefer SUBTLE gradients (5–10% saturation difference between stops).

```swift
// Subtle background gradient — works
LinearGradient(
    colors: [Color(.systemBackground), Color(.secondarySystemBackground)],
    startPoint: .top, endPoint: .bottom
)

// AI cliché — avoid
LinearGradient(colors: [.purple, .blue, .pink], ...)
```

### Color in OKLCH — perceptually-uniform palettes

The problem with hex / RGB / HSL: equal "lightness" values do **not** look equally bright. Pure yellow at HSL 50% L is wildly brighter than pure blue at HSL 50% L. That's why most hand-picked palettes feel uneven — one color always "wins" because the others are actually darker.

**OKLCH** (Oklab Lightness/Chroma/Hue) is perceptually uniform — equal `L` looks equally bright across every hue:
- `L`: 0–1.0 lightness (perceptually uniform)
- `C`: 0+ chroma (saturation independent of hue)
- `H`: 0–360° hue

SwiftUI doesn't expose OKLCH natively yet (as of iOS 26), but the workflow is straightforward:

**1. Design in OKLCH, ship as Display P3 hex.** Pick palettes at [oklch.com](https://oklch.com), convert to hex once, bake into `Color` extensions:

```swift
// All three designed at oklch(0.65 0.18 H) — same perceptual brightness
extension Color {
    static let brandBlue  = Color(.displayP3, red: 0.184, green: 0.490, blue: 0.871) // H=240
    static let brandGreen = Color(.displayP3, red: 0.067, green: 0.561, blue: 0.349) // H=145
    static let brandRed   = Color(.displayP3, red: 0.937, green: 0.349, blue: 0.337) // H=20
}
```

All three feel like *siblings* — no color screams. Try the same with naive RGB picking and one will dominate.

**2. Dark-mode pairs by lowering `L` only.** Keep `C` and `H` constant — the perceived hue stays identical, just darker. HSL-based dark-mode tools shift hue with brightness, producing muddy results.

```
Light: oklch(0.65 0.18 240)  → #2F7DDE
Dark:  oklch(0.45 0.18 240)  → #1A52A8
```

**3. Multi-stop gradients with OKLCH intermediates.** SwiftUI's `LinearGradient(colors:)` interpolates in linear-RGB by default — so yellow→blue passes through **gray** in the middle. Fix: generate stops in OKLCH (where hue rotates smoothly through green→teal) and pass them as explicit `stops:`.

```swift
// Bad — RGB-lerp passes through gray
LinearGradient(colors: [.yellow, .blue], startPoint: .top, endPoint: .bottom)

// Good — OKLCH stops rotate through proper intermediate hues
LinearGradient(
    stops: [
        .init(color: Color(hex: "#FFFF00"), location: 0.00),
        .init(color: Color(hex: "#7BC569"), location: 0.33),  // OKLCH lerp midpoint
        .init(color: Color(hex: "#3A87C0"), location: 0.66),  // OKLCH lerp midpoint
        .init(color: Color(hex: "#0000FF"), location: 1.00),
    ],
    startPoint: .top, endPoint: .bottom
)
```

Generate stops via [culori](https://culorijs.org/) (Node), [oklch.com](https://oklch.com)'s gradient tool, or any OKLCH library — bake the hex into Swift once.

**4. Use Display P3 for vivid colors.** P3 is a wider gamut than sRGB; reds redder, greens greener. Every Apple device since 2017 supports it. iOS auto-degrades to sRGB on older hardware. Almost no apps bother — free polish win.

```swift
Color(red: 1.0, green: 0.2, blue: 0.4)                  // sRGB — bounded gamut
Color(.displayP3, red: 1.0, green: 0.2, blue: 0.4)      // P3 — full screen gamut
```

**A `Color(hex:)` helper** (keep your codebase clean):

```swift
extension Color {
    init(hex: String, opacity: Double = 1.0) {
        var hex = hex.trimmingCharacters(in: .whitespacesAndNewlines)
        if hex.hasPrefix("#") { hex.removeFirst() }
        var rgb: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&rgb)
        self.init(
            .displayP3,
            red:   Double((rgb & 0xFF0000) >> 16) / 255,
            green: Double((rgb & 0x00FF00) >> 8)  / 255,
            blue:  Double( rgb & 0x0000FF)        / 255,
            opacity: opacity
        )
    }
}
```

### Subtle background textures — beyond flat color

A pure flat `Color(.systemBackground)` is fine for utility apps but reads as "generic" for products that want to feel crafted. Stripe, Linear, Mercury, Arc, Things 3, Granola all layer one or more of these techniques.

**The hierarchy of background polish (compose as needed):**

| Layer | Use | Performance |
| --- | --- | --- |
| Solid color | Utility apps, dense lists | Free |
| Subtle gradient (5–10% saturation Δ) | Most product surfaces | Free |
| MeshGradient (iOS 18+) | Onboarding, paywall, splash, hero | Cheap |
| Noise overlay (3–6% PNG or Canvas) | Anti-banding on any gradient | Free (static) |
| Tiled subtle pattern (dots, grain) | Brand-defining surfaces | Cheap (cached) |
| Vignette / corner light | Atmospheric depth | Free |
| Animated TimelineView gradient | Hero moments only | Heavy — cap fps |

**1. MeshGradient — the new primitive (iOS 18+)**

`MeshGradient` places colors at points on a 2D grid and blends organically. Looks hand-painted, not "computer gradient." New gold standard for hero backgrounds.

```swift
MeshGradient(
    width: 3, height: 3,
    points: [
        [0.0, 0.0], [0.5, 0.0], [1.0, 0.0],
        [0.0, 0.5], [0.5, 0.5], [1.0, 0.5],
        [0.0, 1.0], [0.5, 1.0], [1.0, 1.0]
    ],
    colors: [
        .pink.opacity(0.5),   .orange.opacity(0.4), .yellow.opacity(0.3),
        .purple.opacity(0.4), .blue.opacity(0.3),   .mint.opacity(0.3),
        .indigo.opacity(0.4), .teal.opacity(0.3),   .green.opacity(0.2)
    ]
)
.ignoresSafeArea()
```

Animate via `TimelineView` for slow organic drift:

```swift
TimelineView(.animation) { ctx in
    let t = ctx.date.timeIntervalSinceReferenceDate
    MeshGradient(
        width: 3, height: 3,
        points: [
            [0.0, 0.0], [0.5, 0.0], [1.0, 0.0],
            [0.0, 0.5],
            [0.5 + 0.05 * sin(t * 0.4), 0.5 + 0.05 * cos(t * 0.4)],  // drifts
            [1.0, 0.5],
            [0.0, 1.0], [0.5, 1.0], [1.0, 1.0]
        ],
        colors: meshColors
    )
}
```

**2. Noise / film grain — eliminates banding**

Solid gradients on OLED screens BAND visibly. A 3–6% opacity noise overlay breaks the gradient up at the pixel level and adds film-grain texture the eye reads as "rich" without consciously identifying it.

```swift
ZStack {
    LinearGradient(colors: [.purple.opacity(0.2), .pink.opacity(0.1)],
                   startPoint: .top, endPoint: .bottom)

    Image("noise-256")              // 256×256 PNG of fine grain, tileable
        .resizable(resizingMode: .tile)
        .opacity(0.04)
        .blendMode(.overlay)
        .allowsHitTesting(false)
        .ignoresSafeArea()
}
```

**Critical: < 6% opacity.** If you can SEE grain, it's too much. The point is for the eye to read depth without identifying the source. Generate a 256×256 noise PNG once in any image tool (or procedurally via `Canvas` for sharper dark/light adaptation).

**3. Tiled subtle patterns — Linear's dots, Things 3's paper**

Custom `Canvas` view drawn once, cached via `.drawingGroup()`. Adapts to color scheme via semantic colors.

```swift
struct DotGridBackground: View {
    var body: some View {
        Canvas { context, size in
            let spacing: CGFloat = 24
            let dotSize: CGFloat = 1.5
            let color = Color(.label).opacity(0.06)
            for x in stride(from: spacing, to: size.width, by: spacing) {
                for y in stride(from: spacing, to: size.height, by: spacing) {
                    let rect = CGRect(x: x - dotSize/2, y: y - dotSize/2,
                                      width: dotSize, height: dotSize)
                    context.fill(Path(ellipseIn: rect), with: .color(color))
                }
            }
        }
        .drawingGroup()              // rasterize once for perf
        .allowsHitTesting(false)
    }
}
```

Rules: opacity ≤ 8%; small repeats (high frequency); adapts to light/dark via `.label`.

**4. Vignettes & corner lights — "lit from somewhere"**

A `RadialGradient` with `.blendMode(.plusLighter)` adds depth without explicit decoration. Apple Music does this on dark UIs.

```swift
ZStack {
    Color(.systemBackground)

    RadialGradient(
        colors: [Color.white.opacity(0.08), .clear],
        center: .topLeading,
        startRadius: 0, endRadius: 400
    )
    .blendMode(.plusLighter)
    .allowsHitTesting(false)
}
```

Reverse for vignettes (darken edges): `RadialGradient` from `.clear` center → `.black.opacity(0.3)` edges with default blend.

**5. Animated TimelineView gradients — hero moments only**

```swift
TimelineView(.animation) { ctx in
    let phase = ctx.date.timeIntervalSinceReferenceDate * 0.1
    LinearGradient(
        colors: [.purple, .pink, .orange],
        startPoint: UnitPoint(x: 0.5 + 0.4 * cos(phase), y: 0.5 + 0.4 * sin(phase)),
        endPoint:   UnitPoint(x: 0.5 - 0.4 * cos(phase), y: 0.5 - 0.4 * sin(phase))
    )
}
```

Use SPARINGLY — too heavy for every screen. On older devices, prefer `MeshGradient` with point animation (much cheaper) over animated `LinearGradient`.

**The compose pattern:**

A premium paywall background = `MeshGradient` base + noise overlay at 4% + corner light at upper-left with `.plusLighter`. Perceived complexity: low. Actual richness: high. Stack these like layers in Figma — that's the trick.

### Trays adopt the environment

When a sheet, popover, or context menu appears from a themed surface — a dark chat thread, a black-chrome camera UI, a brand-tinted onboarding flow — it must INHERIT that environment's color scheme and tint. A sticker picker over a dark chat should be dark. A confirmation in a camera UI should be black. A modal in branded onboarding should pick up the brand color.

```swift
.sheet(isPresented: $showing) {
    Content()
        .preferredColorScheme(parentScheme)   // inherit explicitly
        .tint(parentTint)
        .presentationBackground(parentSurface)
}
```

The visual environment should follow the user across modal layers. Sudden theme switches are spatially disorienting — the user has to re-orient every time, and the app feels like a collection of pages instead of one place.

---

## 6. Spacing, rhythm & optical alignment

### The 4pt grid

iOS is built on a 4pt grid. Every spacing value should be a multiple of 4: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64.

Common spacings:
- **2pt**: hairline separators, bubble-to-bubble within a group
- **4pt**: tight icon-text gaps
- **8pt**: standard small gap, list-item internal padding
- **12pt**: card internal padding (small)
- **16pt**: card internal padding (standard), section padding
- **20pt**: small section spacing
- **24pt**: standard section spacing, card-to-card
- **32pt**: large section spacing, "breathing" gaps
- **48pt**: hero section spacing
- **64pt+**: marketing pages, large breaks

### Breathing room

The single most common polish mistake: not enough padding around hero elements. **Hero numbers / large titles want 24pt of breathing room above and below.** Not 12pt. Not 16pt. 24pt or more.

```swift
VStack(spacing: 24) {
    HeroNumber("$1,247")
    Caption("Available balance")
}
.padding(.vertical, 32)
```

### Optical alignment

Mathematical alignment ≠ visual alignment. When two shapes of different geometries sit beside each other, they need OPTICAL alignment, not pixel alignment.

**Classic cases:**
- A circle next to a square at the same height: the square LOOKS bigger. Render the square at 92% of the circle's diameter for visual equality.
- Text next to an icon: the icon's optical center is rarely its geometric center. Nudge by 0.5–1pt.
- A "play" triangle inside a circle: the triangle's geometric center is too far left. Nudge right by 1–2pt.

SwiftUI tools:
- `.offset(x: 1, y: 0)` for fine-tuning
- Custom alignment guides for repeated patterns

This is where the eye picks up "considered" vs "generic."

### Asymmetric padding

Cards often look better with MORE bottom padding than top. A card with `.padding(.top, 16).padding(.bottom, 20)` reads as more grounded than `.padding(16)`.

Buttons want MORE horizontal padding than vertical:
- `.padding(.horizontal, 20).padding(.vertical, 12)` for a standard button
- Vertical padding ≈ 0.6× font size; horizontal padding ≈ 1.2× font size

### Hierarchy via spacing

Closer spacing = related. Farther spacing = unrelated. Use this to communicate structure WITHOUT visual chrome (lines, boxes).

```swift
VStack(alignment: .leading, spacing: 4) {
    Text("Title").font(.headline)
    Text("Subtitle").font(.subheadline).foregroundStyle(.secondary)
}
.padding(.bottom, 16) // Bigger gap before next section

VStack(alignment: .leading, spacing: 4) {
    Text("Next title")
    Text("Next subtitle")
}
```

Two `VStack`s with 4pt internal spacing + 16pt between them communicates "two groups" without any divider.

### No layout shift — the polish foundation

The single most jarring "amateur" tell: surrounding elements jumping when something changes inside them. Adapted from Emil Kowalski's web design engineering practice, the iOS-native offenders:

- **Font weight changes that shift width.** A tab that goes from `.regular` (inactive) to `.semibold` (selected) makes the tab WIDER, shifting other tabs. Fix: use a consistent weight + opacity/color to indicate selection, OR explicitly fix the tab width.
- **Adding a badge that bumps siblings.** When an unread count appears on an icon, it should OVERLAY the icon (via `.overlay(alignment: .topTrailing)` with negative offset), not push siblings.
- **Dynamic content reflowing.** A subtitle growing from 1 line to 2 reflows the card height — every other card moves. Fix: reserve space with `.frame(minHeight:)`, or design a layout that gracefully accommodates variable content.
- **Numbers changing widths.** Already covered in §4: always use `.monospacedDigit()` for changing numerics.
- **Loading → loaded layout swap.** Skeleton screens that don't match the real layout cause a layout jump the moment data arrives. Match structurally (see §12).
- **`.font(.body)` swapping to a custom font.** Each font has different metrics — swapping mid-app shifts everything. Pick a font per role and stick with it.

The test: record your app's main flows on a real device. Play back at 0.5×. Anything that JUMPS (not animates — *jumps*) is a layout-shift bug. Fix every one.

---

## 7. SF Symbols & Symbol Effects

SF Symbols is an underused superpower. 6000+ icons, all weight-matched to SF Pro, all animatable.

### Rendering modes

- `.symbolRenderingMode(.monochrome)` — single color (default)
- `.symbolRenderingMode(.hierarchical)` — secondary/tertiary opacities within one symbol (great for cards)
- `.symbolRenderingMode(.palette)` — multi-color with explicit colors
- `.symbolRenderingMode(.multicolor)` — uses each symbol's designed colors

```swift
Image(systemName: "wifi")
    .symbolRenderingMode(.hierarchical)
    .foregroundStyle(.blue)
// Renders with full-strength blue for the strong waves, faded blue for weaker
```

Hierarchical mode is the easiest polish win — your icons get depth for free.

### Symbol Effects (iOS 17+)

| Effect | Trigger | Use |
| --- | --- | --- |
| `.symbolEffect(.bounce, value: trigger)` | One-shot | Confirmation taps (like, save, send) |
| `.symbolEffect(.pulse)` | Continuous, **active state only** | Recording, processing, "listening" — NOT decoration |
| `.symbolEffect(.variableColor)` | Animation | Wi-Fi loading, signal acquiring |
| `.symbolEffect(.scale.up, isActive: ...)` | State-based | Emphasis on important state |
| `.symbolEffect(.appear / .disappear)` | View visibility | Polished on/off |
| `.symbolEffect(.wiggle, value: trigger)` (iOS 18+) | One-shot | Playful "no" gesture |
| `.symbolEffect(.rotate, value: trigger)` | One-shot | Refresh, reload |
| `.contentTransition(.symbolEffect(.replace))` | Symbol change | Play ↔ Pause, Heart ↔ Heart Fill |

**Note**: `.symbolEffect(.breathe)` exists (iOS 18+) but **avoid it** — see anti-pattern below.

Examples:
```swift
// Heart like
Image(systemName: liked ? "heart.fill" : "heart")
    .foregroundStyle(liked ? .red : .gray)
    .contentTransition(.symbolEffect(.replace))
    .symbolEffect(.bounce, value: liked) // bounce on the change

// Wi-Fi loading
Image(systemName: "wifi")
    .symbolRenderingMode(.hierarchical)
    .symbolEffect(.variableColor.iterative, isActive: isConnecting)

// Recording dot
Image(systemName: "record.circle.fill")
    .foregroundStyle(.red)
    .symbolEffect(.pulse, isActive: isRecording)
```

### Icon motion: DO morph, DON'T breathe

Modern SF Symbols are the most powerful animatable iconography on any mobile platform. But the failure mode is consistent across AI-generated apps and template builds: **ambient scale-pulsing and "breathing" animations on icons that aren't doing anything**. They always look bad. They scream "generic," they age poorly, and they pull the eye for no reason.

**DO** — motion must be **triggered** by user action or **anchored** to a real state change:

| Pattern | Use |
| --- | --- |
| `.contentTransition(.symbolEffect(.replace))` | The single most useful effect. Morph one symbol into another on state change: Play ↔ Pause, Heart ↔ Heart.Fill, Bookmark ↔ Bookmark.Fill, Eye ↔ Eye.Slash. Looks expensive, costs nothing. |
| `.symbolEffect(.bounce, value: trigger)` | Single bounce on user action: tap to like, tap to save, send confirmation. Always paired with `.sensoryFeedback`. |
| `.symbolEffect(.pulse, isActive: isRecording)` | ACTIVE-STATE indicator only — when something is genuinely happening (recording, AI processing, listening for voice input). Stops the moment the state ends. |
| `.symbolEffect(.variableColor.iterative, isActive: isConnecting)` | Loading / acquiring (Wi-Fi connecting, signal searching). Communicates "in progress." |
| `.symbolEffect(.wiggle, value: errorTrigger)` | Playful denial — "no, you can't drop that here." Use sparingly. |
| `.symbolEffect(.rotate, value: refreshTrigger)` | One-shot rotation on refresh / reload action. |

**DON'T** — never animate icons that aren't responding to a real event:

- ❌ **`.symbolEffect(.breathe)` for ambient "calm presence"** — looks like a screensaver. The icon pulses for no reason. Every "AI meditation app" template uses this. Skip it.
- ❌ **Continuous scale-pulse on a heart, star, or favorite icon when nothing is happening** — feels like the icon is begging for a tap. Trust the icon to communicate via its shape alone.
- ❌ **`.symbolEffect(.pulse, options: .repeating)` on idle UI** — pulse means "active right now." Repeating it forever makes "active" meaningless.
- ❌ **Bouncing the tab bar icon you're currently on** — drains attention from content. Apple's own tab bar doesn't do this.
- ❌ **Animating ALL the icons in a row to draw attention to one** — the eye picks up the motion, not the meaning. If one icon is important, isolate it; don't animate the whole row.

**The rule**: every icon animation must answer the question "what just happened?" If the answer is "nothing," remove it. Static icons are not boring — they're confident. Animated icons signal an event. When EVERYTHING signals, NOTHING signals.

The Apple-native litmus test: open the system Messages, Photos, or Mail app. Watch how few icon animations they use. The polish is in restraint.

### Variable symbols

Many SF Symbols support a `variableValue` from 0.0 to 1.0:
```swift
Image(systemName: "speaker.wave.3.fill", variableValue: volume)
// Renders 0, 1, 2, or 3 sound waves based on volume
```

Perfect for: signal strength, battery, volume, brightness, progress indicators that have a natural symbolic representation.

### Custom symbols

Make your brand's icons as SF Symbols (Asset Catalog → Add → Symbol Image, or use Apple's SF Symbols app to export a template). Your custom symbols get all the same effects, rendering modes, weight-matching, and Dynamic Type behavior.

Critical: design your custom symbols at the variable optical sizes (S, M, L). Don't just import one PNG.

### When NOT to use SF Symbols

For your APP ICON, hero illustrations, and onboarding screens — use custom artwork. SF Symbols are functional. They are not your brand.

---

## 8. Haptics — `.sensoryFeedback`

iOS 17 added `.sensoryFeedback` — the modern, SwiftUI-native haptic API. Use it.

```swift
.sensoryFeedback(.selection, trigger: selectedTab)
.sensoryFeedback(.success, trigger: didSave)
.sensoryFeedback(.impact(weight: .light), trigger: tapCount)
```

### Available styles

| Style | Use |
| --- | --- |
| `.selection` | Selection changes — tabs, pickers, segmented controls |
| `.success` | Successful completion (saved, sent, posted) |
| `.warning` | About to be destructive |
| `.error` | Failed action |
| `.impact(weight: .light)` | Light tap |
| `.impact(weight: .medium)` | Standard tap |
| `.impact(weight: .heavy)` | Critical or "heavy" event |
| `.impact(flexibility: .soft)` | Even softer |
| `.impact(flexibility: .rigid)` | Sharp click (toggle, detent) |
| `.start` | Beginning of a continuous interaction |
| `.stop` | End of one |
| `.alignment` | Snap to alignment / detent |
| `.decrease` / `.increase` | Step-wise count changes |
| `.levelChange` | Crossing a threshold (e.g., next stop on a slider) |
| `.pathComplete` | Finished a path (lock pattern, signature) |

### The full polish pattern: tap → animate → haptic → sound

When the user taps a meaningful action:
1. **Visual** fires immediately (scale to 0.97 on touch-down).
2. **Haptic** fires on touch-down (light) AND touch-up (style depending on action).
3. **Animation** plays the result (e.g., heart fills).
4. **Sound** plays only if it adds meaning (rare). See §9.
5. **Confirmation** appears (e.g., toast, badge) with its own subtle haptic.

```swift
Button {
    liked.toggle()
} label: {
    Image(systemName: liked ? "heart.fill" : "heart")
        .foregroundStyle(liked ? .red : .secondary)
        .scaleEffect(pressed ? 0.92 : 1.0)
        .contentTransition(.symbolEffect(.replace))
        .symbolEffect(.bounce, value: liked)
}
.buttonStyle(.plain)
.sensoryFeedback(.impact(weight: .light), trigger: liked)
.animation(.snappy(duration: 0.2), value: liked)
.pressAction { pressed = $0 } // custom modifier; see §10
```

### Combining haptics

For complex moments, layer haptics:
```swift
.sensoryFeedback(trigger: messageStatus) { _, new in
    switch new {
    case .sent: return .impact(weight: .light)
    case .delivered: return .impact(flexibility: .soft)
    case .read: return .success
    case .failed: return .error
    default: return nil
    }
}
```

### CoreHaptics for the truly bespoke

For multi-step patterns, audio-synced haptics, or > 1s continuous haptics, drop down to CoreHaptics (see [interaction-primitives](../interaction-primitives/SKILL.md)).

Memorable moments worth a custom AHAP:
- App's signature send/receive (Telegram has one)
- First-launch celebration
- Critical milestone (your 100th workout, first $1,000 saved)
- A signature physical interaction (Halide's burst-mode "ratchet" feel)

### When NOT to haptic

- Cold app launch (engine is asleep; will lag).
- Every cell scroll (vibrates the phone — annoying).
- "New message" notifications when the app is foreground (the user is already looking).
- Saved settings (the toggle change already haptics).

The rule: **fire on user-initiated, meaningful changes only.**

---

## 9. Sound design

iOS apps generally avoid in-app sound. The system handles ringtones, notifications, keyboard clicks. Adding your own sound is risky — the user has their volume up for a reason, and surprise audio breaks trust.

**When sound IS appropriate:**
- **Camera shutter** (if you have one — required for camera apps in some jurisdictions; Apple's Camera plays a click).
- **Voice messages** — playback obviously needs sound, but the SEND haptic should be silent.
- **Games / immersive experiences** — different rules.
- **Confirmation moments that match a real-world sound** — e.g., a "ka-ching" for completed payment (Cash App does this).
- **Sound design as core feature** — meditation apps (Calm, Oak), audio products (podcasts, Apple Music).

**Rules when you DO use sound:**
1. **Match haptic and sound** — they should fire together at < 10ms apart. The pairing creates the "physicality" Family talks about.
2. **Respect silent mode** — observe `AVAudioSession.Category.ambient` so the user's silent switch works. NEVER play through `.playback` for incidental UI sounds.
3. **Keep it under 200ms** — UI sounds should be a single discrete event, not a chord.
4. **Provide a setting to disable them** — even if defaulted on, users should be able to turn them off.
5. **Royalty-free or custom-composed** — never use stock sounds the user will recognize from another app.

```swift
import AudioToolbox

// System sound IDs work for one-off effects
AudioServicesPlaySystemSound(1057) // tink

// Custom sounds via AVAudioPlayer
let url = Bundle.main.url(forResource: "celebration", withExtension: "caf")!
let player = try AVAudioPlayer(contentsOf: url)
try AVAudioSession.sharedInstance().setCategory(.ambient, options: [.mixWithOthers])
player.play()
```

For the truly committed: pair sound with haptic via CoreHaptics' `audioResourceID` — they then play *perfectly* synced (sample-accurate).

---

## 10. Touch & gesture polish

### Tap target minimum: 44 × 44pt

Even if your icon is 24pt, give it a 44pt tap area:
```swift
Image(systemName: "xmark")
    .frame(width: 44, height: 44)
    .contentShape(Rectangle())
    .onTapGesture { ... }
```

`.contentShape(Rectangle())` is the critical part — without it, the tap only registers on the actual icon glyph (24pt), not the padding around it.

### Visible press states

EVERY tappable element should respond to touch-down, not just touch-up.

```swift
struct PressableButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.96 : 1.0)
            .opacity(configuration.isPressed ? 0.85 : 1.0)
            .animation(.spring(duration: 0.16, bounce: 0), value: configuration.isPressed)
    }
}

Button("Continue") { }
    .buttonStyle(PressableButtonStyle())
```

For more granular control (e.g., haptic on touch-down):
```swift
struct PressGesture: ViewModifier {
    @Binding var isPressed: Bool
    func body(content: Content) -> some View {
        content
            .gesture(
                DragGesture(minimumDistance: 0)
                    .onChanged { _ in isPressed = true }
                    .onEnded { _ in isPressed = false }
            )
    }
}
```

### Rubber-banding

Native iOS scrolling rubber-bands at the edges. When you build custom horizontal carousels or drag-dismissible sheets, replicate this:

```swift
@GestureState private var dragOffset: CGFloat = 0

DragGesture()
    .updating($dragOffset) { value, state, _ in
        let raw = value.translation.height
        // Rubber-band: increasingly resist past 0
        if raw < 0 {
            state = raw / 3 // 1/3 the actual drag past the boundary
        } else {
            state = raw
        }
    }
```

The function `raw / (1 + abs(raw) / 200)` gives a smoother rubber-band asymptote.

### Drag with momentum

When releasing a drag, carry the gesture's velocity into the spring:
```swift
.onEnded { value in
    let velocity = value.predictedEndLocation.y - value.location.y
    withAnimation(.interpolatingSpring(stiffness: 320, damping: 28, initialVelocity: velocity / 100)) {
        offset = .zero
    }
}
```

### Swipe-to-dismiss with progressive feedback

As the user drags a sheet down to dismiss, the background should darken or fade with linear opacity tied to drag distance. Haptic at the dismiss threshold:

```swift
.gesture(
    DragGesture()
        .onChanged { value in
            offset = max(0, value.translation.height)
            backgroundOpacity = 1 - min(offset / 300, 1) * 0.8
            // Haptic at dismiss threshold
            if offset > 120 && !pastThreshold {
                pastThreshold = true
                UIImpactFeedbackGenerator(style: .soft).impactOccurred()
            }
        }
        .onEnded { value in
            if offset > 120 || value.predictedEndLocation.y > 600 {
                dismiss()
            } else {
                withAnimation(.spring(duration: 0.32, bounce: 0)) {
                    offset = 0
                    backgroundOpacity = 1
                }
            }
        }
)
```

### Pinch to zoom with rotation/translation

For photo zoom, layer three simultaneous gestures:
```swift
let zoom = MagnificationGesture()
    .onChanged { scale = $0 }
let drag = DragGesture()
    .onChanged { offset = $0.translation }

photo.gesture(SimultaneousGesture(zoom, drag))
```

The polish detail: when scale drops below 1.0, snap back with rubber-band; when scale exceeds max, rubber-band again. Use `.interpolatingSpring`.

### Keyboard return key — `.submitLabel`

When a text input is part of a form, search bar, or composer, the keyboard's return key should show the right verb — not a generic Return arrow.

```swift
TextField("Email", text: $email)
    .submitLabel(.next)
    .onSubmit { focusedField = .password }

TextField("Search", text: $query)
    .submitLabel(.search)
    .onSubmit { runSearch() }
```

Available labels: `.done`, `.go`, `.next`, `.return`, `.search`, `.send`, `.join`, `.route`, `.continue`. Match the verb to the action. This is the kind of micro-detail users don't consciously notice but which makes the keyboard feel native and the form feel finished.

For multi-line text where Return should insert a newline, don't override — let the system handle it. Pair with a dedicated send button instead.

---

## 11. Image & media polish

### Fade-in on load

Images appearing instantly look like a bug. Cross-fade them:

```swift
AsyncImage(url: url, transaction: Transaction(animation: .easeOut(duration: 0.32))) { phase in
    switch phase {
    case .empty:
        placeholderView
    case .success(let image):
        image.resizable().scaledToFill()
            .transition(.opacity)
    case .failure:
        errorView
    @unknown default: EmptyView()
    }
}
```

Or use Kingfisher / Nuke for production-grade image loading with built-in fade and caching.

### Blurhash / low-res progressive

For premium feel: show a blurred low-resolution placeholder, then cross-fade to the high-res image.

```swift
ZStack {
    BlurhashView(hash: post.blurhash) // small, fast — decoded from a tiny string
    AsyncImage(url: post.imageURL)
        .transition(.opacity.animation(.easeOut(duration: 0.4)))
}
```

Blurhash is a tiny string (20–30 chars) encoded server-side, decoded client-side to a blurred preview. Instagram, Wolt, and many premium apps use this.

### Subtle inset shadow on photo cells

Photos floating in a grid often need an extremely subtle inner stroke at the edge so the photo doesn't blend into the background (especially when the photo edge is white).

```swift
Image(...)
    .clipShape(RoundedRectangle(cornerRadius: 14, style: .continuous))
    .overlay(
        RoundedRectangle(cornerRadius: 14, style: .continuous)
            .inset(by: 0.5)
            .stroke(Color.black.opacity(0.05), lineWidth: 0.5)
    )
```

### Vignettes for hero images

For hero photos with text overlaid, add a subtle radial vignette to keep the text readable without darkening the whole image:

```swift
Image(...)
    .overlay(
        LinearGradient(
            colors: [.clear, .black.opacity(0.5)],
            startPoint: .center,
            endPoint: .bottom
        )
    )
```

The text reads, the image's hero remains visible.

### Smooth zoom with `.scaledToFill()` + clipping

When a user pinches an image, you want the IMAGE to zoom, not the container. Use `.scaledToFill()` + `.clipped()` + `.scaleEffect()`:

```swift
Image(...)
    .resizable()
    .scaledToFill()
    .frame(width: containerWidth, height: containerHeight)
    .clipped()
    .scaleEffect(zoom)
    .gesture(magnification)
```

### Image grid scroll performance

For grids of 100+ images, use `LazyVGrid` or `LazyHGrid` and pre-fetch thumbnails. Use `PHCachingImageManager` for PhotoKit assets, or Kingfisher's prefetcher for remote URLs.

---

## 12. Loading states

### Skeleton screens with shimmer

Replace spinner with a skeleton that MATCHES the layout of the upcoming content.

```swift
struct SkeletonCell: View {
    @State private var shimmer = false
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            RoundedRectangle(cornerRadius: 8)
                .fill(Color(.systemGray5))
                .frame(width: 160, height: 16)
            RoundedRectangle(cornerRadius: 6)
                .fill(Color(.systemGray5))
                .frame(width: 120, height: 12)
        }
        .overlay(
            LinearGradient(
                colors: [.clear, Color.white.opacity(0.3), .clear],
                startPoint: .leading, endPoint: .trailing
            )
            .rotationEffect(.degrees(20))
            .offset(x: shimmer ? 200 : -200)
            .animation(.linear(duration: 1.2).repeatForever(autoreverses: false), value: shimmer)
        )
        .mask(content) // mask the shimmer to the skeleton shape
        .onAppear { shimmer = true }
    }
}
```

**Critical: skeletons must structurally match the real content.** A skeleton with 3 lines while the real content has 5 = broken illusion. If the real card has an avatar, a title, and a subtitle — the skeleton has a circle (avatar), a rect (title), and a smaller rect (subtitle), in the same positions.

### Optimistic UI

For ANY action initiated by the user, show the result IMMEDIATELY — before the server responds. If the server later fails, reconcile.

Examples:
- Like a post: heart fills instantly. Server call happens in background.
- Send a message: bubble appears in conversation instantly. Network later.
- Save a setting: toggle flips instantly. Persistence later.

The principle: **the user's action causes the visible effect. Network is implementation detail.**

```swift
func like() {
    let original = isLiked
    isLiked = true // optimistic
    Task {
        do {
            try await api.like(post.id)
        } catch {
            await MainActor.run {
                isLiked = original // revert
                showErrorBanner()
            }
        }
    }
}
```

### Progressive disclosure of long-running operations

For operations > 1 second:
- 0–500ms: silent. No spinner. Just appear done when done.
- 500ms–2s: subtle inline indicator (a small progress dot, an `.symbolEffect(.pulse)` on the relevant icon).
- 2s+: explicit progress indicator with progress bar IF you can compute progress, otherwise an indeterminate spinner.
- 10s+: consider a Live Activity (see [interaction-primitives](../interaction-primitives/SKILL.md#4-live-activities)).

### The spinner of last resort

If you MUST use a spinner, use `ProgressView()` (system-styled) — not a custom one. System spinners adapt to color scheme, accent color, and Reduce Motion automatically.

For full-screen loading, embed in a `VStack` with a subtle label below — "Loading…" is fine; "Hold on, we're crunching the numbers..." is not.

### The spinner travels to where the result will appear

One of the highest-leverage polish patterns, adapted from [Family's design philosophy](https://benji.org/family-values). When a user action initiates a load, the loading indicator should NOT sit at the location of the action — it should migrate to where the user will *look for* the result.

- **Submit a transaction** → spinner migrates to the Activity tab icon (and stays as a subtle dot until complete).
- **Save a photo** → spinner rides the thumb-flight to the gallery button.
- **Send a message** → spinner appears inside the optimistically-rendered bubble, not on the send button.
- **Export a video** → progress migrates to a Live Activity in the Dynamic Island, freeing the user to continue.
- **Sync in the background** → progress shown as a subtle ring around the relevant tab icon.

The user's eye follows one location. Anchor the loading state to the DESTINATION, not the TRIGGER. This pattern applies across the four skills in this folder — `camera-and-photos` uses it for save flights, `chat-and-messaging` for message status, `interaction-primitives` for Live Activity confirmation.

### Vary heights of stacked layers

When sheets stack (a confirm dialog over a settings sheet over the main view), each layer MUST be a visibly different height than the layer beneath. Two identical-height sheets read as "one layer that swapped" — the user loses spatial orientation entirely.

```swift
// Good — first sheet 70% height, confirmation 35% height
.sheet(isPresented: $showSettings) {
    SettingsView()
        .presentationDetents([.fraction(0.7)])
        .sheet(isPresented: $showConfirmation) {
            ConfirmationView()
                .presentationDetents([.fraction(0.35)])
        }
}
```

Apple's built-in `.medium` and `.large` detents handle this naturally. If you customize, ensure each subsequent layer is at least 25% smaller (or larger) than the parent. The size difference is what communicates "you went deeper" — without it, the user thinks the app glitched.

---

## 13. Empty states

> "Empty states are first impressions." — Family design philosophy

The empty state is what the user sees BEFORE they've done anything. It's the first impression. It's almost never given the care of the hero.

### The three things every empty state needs

1. **A friendly illustration or symbol** — NOT a generic ![empty box]. A small custom illustration (commissioned art, an SF Symbol with `.bounce`, or a simple line drawing) that matches your brand.
2. **A clear, warm explanatory line** — "Nothing here yet" is the bare minimum. Better: "Your first note is one tap away." Best: a sentence in your brand voice that explains WHAT to do.
3. **An invitation to act** — either a button (with a clear primary action) OR an animated arrow pointing at the action they should take (in a navigation bar etc).

```swift
struct EmptyNotesView: View {
    @State private var bobbing = false
    var body: some View {
        VStack(spacing: 24) {
            Image(systemName: "note.text")
                .font(.system(size: 64))
                .foregroundStyle(.tertiary)
                .offset(y: bobbing ? -4 : 4)
                .animation(.easeInOut(duration: 1.8).repeatForever(autoreverses: true), value: bobbing)

            VStack(spacing: 6) {
                Text("Your first note is waiting")
                    .font(.title3.weight(.semibold))
                Text("Tap the + button to capture a thought.")
                    .font(.callout)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
            .padding(.horizontal, 32)

            Button {
                createNote()
            } label: {
                Label("New Note", systemImage: "plus")
            }
            .buttonStyle(.borderedProminent)
            .controlSize(.large)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .onAppear { bobbing = true }
    }
}
```

### Variations

- **Empty search results**: explain WHAT was searched. "No results for 'apricot'. Try a different word?"
- **Empty inbox**: celebrate. "Inbox zero. Enjoy it." with a subtle illustration of a person at rest.
- **Empty error state**: separate from empty success. "Something went wrong loading your data. Pull to retry."
- **Empty paid feature**: explain what unlocks it. "Pro members can save up to 100. Upgrade for unlimited."

### Animated arrows pointing to the right place

For first-launch empty states, an animated arrow pointing toward the action button is high-impact. Use a subtle horizontal bob:

```swift
Image(systemName: "arrow.down")
    .font(.title2)
    .foregroundStyle(.secondary)
    .offset(y: bobbing ? 4 : -4)
    .animation(.easeInOut(duration: 1.2).repeatForever(autoreverses: true), value: bobbing)
```

Position it pointing at the FAB / tab bar action / "+" button.

---

## 14. Celebrating completions

Don't celebrate every save. Celebrate the moments worth a story.

> **The 100× rule (from Emil Kowalski's design engineering practice):** if a user will see this interaction 100+ times a day, *don't animate it*. Daily-frequency actions should be near-silent — no spring, no haptic, just instant response. The animation and delight budget belongs to the rare, meaningful moments. Inverting this — adding micro-delight to every list scroll and every save — produces apps that feel exhausting after a week. The rarer the event, the bigger the celebration can be.

### The Delight-Impact Curve

Plot frequency vs. delight:
- **Daily (likes, saves, sends, scrolls)**: subtle. Haptic + tiny scale. No confetti.
- **Weekly (completed a workout, hit a streak day)**: memorable. A small custom animation. A satisfied phrase.
- **Monthly (paid bill, finished course module)**: bigger moment. Full-screen success card. Custom illustration.
- **Once or rare (first signup, completed onboarding, 100-day streak)**: THEATRICAL. Confetti, sound, custom animation. Worth a screenshot.

### Confetti — when and how

Use `SwiftUI` particle effects with `CAEmitterLayer` (UIKit-backed) or modern SwiftUI `KeyframeAnimator` choreography.

For a quick win, use a confetti library (e.g., `ConfettiSwiftUI`):
```swift
@State private var confetti = 0

ZStack {
    successContent
    ConfettiCannon(counter: $confetti, num: 80, colors: [.red, .blue, .yellow, .green, .pink])
}
.onAppear { confetti += 1 }
```

**Rules:**
- Confetti is reserved for moments worth a screenshot.
- Duration: 1.5–3s. Then it should be GONE.
- Pair with `.success` sensory feedback + a sound if you have one.
- Color palette: pick 4–6 colors from your brand or universal celebration colors.
- Particle count: 60–120. More feels overwhelming.

### Custom celebration animations

For brand-defining moments, commission a custom animation. Things 3 has a satisfying "tick" animation when you complete a task. Apple Fitness has the ring closure animation. These are signature moments worth investing in.

Use Lottie / Rive / pure SwiftUI keyframes:
```swift
KeyframeAnimator(initialValue: AnimationValues()) { values in
    starShape
        .scaleEffect(values.scale)
        .rotationEffect(values.rotation)
} keyframes: { _ in
    KeyframeTrack(\.scale) {
        SpringKeyframe(1.4, duration: 0.3, spring: .bouncy)
        SpringKeyframe(1.0, duration: 0.6, spring: .smooth)
    }
    KeyframeTrack(\.rotation) {
        LinearKeyframe(.degrees(360), duration: 0.9)
    }
}
```

### Mobbin references

- [Headway daily mission complete](https://mobbin.com/flows/9763b98a-b096-4954-9a98-44602cef6d07) — confetti + checklist
- [Hyundai Card story](https://mobbin.com/flows/53aabea6-05d9-4d1a-8fd8-e3d3cd87d420) — illustrated 3-month anniversary

---

## 15. Onboarding polish

The onboarding is when the user decides if you're a Real App.

### Rules

1. **One purpose per screen.** Each screen does ONE thing. Title + visual + (optional) input + (optional) button.
2. **No more than 4–5 screens.** Anything longer = bail.
3. **A spring transition between screens** — slide horizontal with a subtle parallax effect on the visual.
4. **Show, don't tell.** Use visuals (hero images, illustrations, looped video clips) to demo what the app does — not bullet-point lists.
5. **Permissions deferred.** Don't ask for camera/notifications/contacts during onboarding. Defer until the user is in a context where it makes sense.

### Premium onboarding patterns to study

- **Apple Music** ([Mobbin](https://mobbin.com/flows/3afd5e80-566c-4c10-b466-ad3a24c4076f)) — minimal, brand-forward, drops you into the experience fast.
- **Headway** ([Mobbin](https://mobbin.com/flows/69e7e5d7-fc79-4263-afbb-a4a2f67acd5a)) — illustrated journey, soft animations, progressive disclosure.
- **bless.** ([Mobbin](https://mobbin.com/flows/e13dcdd7-ceb8-4577-8ed4-f89251fd47c3)) — dark theme, single hero illustration per screen, "go!" instead of "continue".
- **Apple TV / Fitness onboarding** — sets a high bar with high-quality video previews.

### Progress indicator

For a 4-step onboarding, show 4 dots at the top — current step filled, others empty. NOT a progress bar (too utilitarian).

```swift
HStack(spacing: 8) {
    ForEach(0..<totalSteps, id: \.self) { i in
        Capsule()
            .fill(i == currentStep ? Color.accentColor : Color(.systemGray4))
            .frame(width: i == currentStep ? 24 : 8, height: 8)
            .animation(.snappy(duration: 0.32), value: currentStep)
    }
}
```

The active dot is wider — visually communicates "you are here" without text.

### First-launch celebration

When the user completes onboarding, mark it. A small confetti, a "Welcome" hero, a personalized first-screen experience. This is the moment they decided to trust you.

---

## 16. Paywall polish

A premium paywall converts. Polish matters here MORE than anywhere else.

### Components of a premium paywall

1. **Hero visual** — a screenshot/video of the feature they're missing, or a beautiful illustration evoking the benefit (peace, productivity, creativity).
2. **Value props as bullet points** — 3–4 max. Each with a small icon. Use SF Symbols + brand colors.
3. **Comparison table** (optional) — for highlighting Pro vs Free OR Pro vs alternatives (a competitor's pricing).
4. **Price tiers** — 2–3 options. Pre-select the recommended one with a "POPULAR" or "BEST VALUE" badge.
5. **Trial signal** — "7 days free, then $X/year" is more effective than "$X/year".
6. **Trust signals** — "App of the Day", "App Store Editor's Choice", "4.9★ on the App Store" with star count.
7. **CTA** — bold, full-width, descriptive. "Start my 7-day free trial" beats "Continue".
8. **Restore purchases link** — small, subtle, always visible.
9. **Terms link** — required by Apple. Footer, gray, small.
10. **Single dismiss action** — × in the top-right OR a back arrow. NEVER make it hard to close (Apple will reject).

### Polish details

- **Animate the value props in with stagger** — each prop slides in 80ms after the previous.
- **Animate the selected tier** — when the user taps a tier, the others dim slightly and the chosen one scales up + gets a subtle border glow.
- **Confetti on subscribe success** — see §14.
- **Spring transitions between paywall states** — never abrupt loading screens. If purchase processing, show inline spinner inside the CTA button.

### Mobbin references

- [Headway paywall](https://mobbin.com/flows/69e7e5d7-fc79-4263-afbb-a4a2f67acd5a) — illustrated, with discount badge
- [Ahead paywall](https://mobbin.com/flows/4d5e054d-b7cc-4ad8-be54-adfb606d1986) — comparison vs Starbucks/Therapy as creative value framing
- [bless. premium](https://mobbin.com/flows/e13dcdd7-ceb8-4577-8ed4-f89251fd47c3) — dark theme, contextual offer

---

## 17. Settings polish

Settings is where most apps stop caring. Don't.

### Native sectioned list

Use `Form { Section { ... } }` — it's the native iOS look for settings. Don't reinvent.

```swift
Form {
    Section {
        Toggle("Notifications", isOn: $notificationsEnabled)
        NavigationLink("Sounds & Haptics", destination: SoundSettings())
    }

    Section("Account") {
        NavigationLink("Profile", destination: ProfileSettings())
        NavigationLink("Privacy", destination: PrivacySettings())
    }

    Section {
        Button("Send Feedback", action: sendFeedback)
        Button("Rate \(appName)", action: rateApp)
    } header: {
        Text("Help")
    } footer: {
        Text("Made with care in [City].")
            .font(.footnote)
            .foregroundStyle(.tertiary)
    }
}
.formStyle(.grouped) // iOS 16+
```

### Polish details

- **Header illustrations** — for a premium feel, the top section of settings can have a header image (e.g., your app icon, large, centered). Adds personality.
- **Status pills** — show current state inline: "Notifications: Allowed", "Pro: Active until June 2026".
- **Section footers** — use them for context: "Your data is stored on-device only" beneath a privacy toggle.
- **Destructive sections** — "Sign Out" and "Delete Account" should be in their OWN section at the bottom, in red.
- **About section** — at the very bottom, include: app version, build, credits, social links, "Made with ♥ in [City]". This is the signature.

### Subtle touches that signal craft

- Tapping the app version 5 times reveals a hidden debug screen (developer easter egg).
- Tap the app icon header → rotates 360° with bounce.
- Pull-to-refresh on settings → resets a setting to default with a subtle haptic.

### The "credits" page

A great app has a credits page. A list of the people who made it, what they did. A photo of the team. A thank-you to the alpha testers. This is the page that converts a customer into an evangelist.

---

## 18. Microcopy & voice

Words are part of the design. Bad copy ruins polished UI.

### The principles

1. **Say less.** Every word is a tax. If a label is 3 words, try 2. If 2, try 1.
2. **Use the user's words.** Match their mental model. If you're a banking app, "Transfer" beats "Initiate Payment".
3. **Be specific.** "Saved" is fine. "Saved to Inbox" is better. "Saved 2 minutes ago" is best.
4. **Avoid bureaucracy.** "Submit", "Proceed", "Enable", "Configure" — these are words from forms, not apps. Use "Send", "Continue", "Turn on", "Set up".
5. **Have a voice.** Anthropic-style precision. Apple-style warmth. Stripe-style competence. Pick one and commit.

### Voice examples

**Apple's voice** — warm, direct, lowercase-when-friendly:
- "Welcome back."
- "Looks like there's nothing here. Yet."
- "Your photos are safe."

**Stripe's voice** — precise, confident, builderly:
- "Run your business in real time."
- "Stripe handles the complicated stuff."
- "Built for developers, used by 4 million businesses."

**Linear's voice** — opinionated, concise:
- "Built for software teams."
- "Linear is fast. Other tools aren't."

**Family's voice** — warm, simple, playful:
- "Let's get you started."
- "Done."
- "Just one more thing."

### Microcopy patterns worth memorizing

| Bad | Good |
| --- | --- |
| "An error occurred." | "We couldn't load this. Tap to retry." |
| "Are you sure you want to delete this?" | "Delete 'Project X'? This can't be undone." |
| "No items." | "Your first item is one tap away." |
| "Loading..." | (nothing under 500ms; "One sec." past that) |
| "Please enter a valid email." | "That email looks off. Mind double-checking?" |
| "Submit" | (depends on action — "Sign Up" / "Save" / "Send") |
| "OK" | (depends — "Got it" / "Continue" / sometimes nothing, just dismiss) |
| "An update is available." | "Things 3 has a new feature. Tap to read more." |
| "Successfully saved." | "Saved." |

### Capitalization

- **Title Case** for nav titles, section headers, button labels: "New Note", "Account Settings".
- **Sentence case** for body, hints, descriptions: "Tap to add a new note."
- **lowercase** for an intentionally casual brand voice (Family, bless.).

NEVER MIX. Pick one and apply consistently.

### Punctuation

- Buttons / nav titles: no terminal punctuation. "Continue" not "Continue."
- Body text: standard punctuation. Always end full sentences with periods.
- Errors: end with a period. Severity matters.
- Toasts: usually no terminal punctuation. "Saved" not "Saved."

---

## 19. Accessibility is polish

Accessibility is the ULTIMATE polish — it requires you to think about every interaction from multiple perspectives.

### Reduce Motion

Always provide an alternative path for animations:
```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

withAnimation(reduceMotion ? .easeInOut(duration: 0.2) : .spring(duration: 0.42, bounce: 0.18)) {
    isExpanded.toggle()
}
```

For hero animations: when Reduce Motion is on, replace `matchedGeometryEffect` with a fast crossfade (180ms `.easeInOut`).

### Reduce Transparency

When ON, the user wants opaque backgrounds (no `.thinMaterial`). Replace with solid fills:
```swift
@Environment(\.accessibilityReduceTransparency) var reduceTransparency

.background(reduceTransparency ? Color(.systemBackground) : .thinMaterial)
```

### Increase Contrast

iOS automatically adjusts semantic colors. If you've used `.primary`, `.secondary`, `Color(.label)` etc., your app already adapts. If you've hard-coded grays, you're broken.

### Dynamic Type

EVERY text label should use a semantic font style (`.body`, `.caption`, etc.) — not hardcoded sizes. Then test with the largest accessibility size:

```swift
ContentSizeCategory.accessibilityExtraExtraExtraLarge
```

Things that break at large Dynamic Type:
- Fixed-height buttons (set min height, not fixed)
- Horizontal layouts with text labels (consider vertical wrap)
- Truncated text (allow multi-line or use `.minimumScaleFactor`)

### VoiceOver — labels that tell a story

Bad: `Image("heart-icon").accessibilityLabel("heart")`.
Good: `.accessibilityLabel(isLiked ? "Unlike post" : "Like post")` + `.accessibilityHint("Double tap to \(isLiked ? "remove your like" : "add your like")")`.

Better: group related elements so VoiceOver reads them as one:
```swift
HStack {
    Image(systemName: "heart.fill")
    Text("234")
}
.accessibilityElement(children: .combine)
.accessibilityLabel("234 likes")
```

For cells: combine the entire cell into one VO element with a clear, descriptive label that includes context (status, timestamp).

### Tap targets

44×44pt minimum. Use `.contentShape(Rectangle())` to make tap targets bigger than visual icons.

### Color contrast

WCAG AA = 4.5:1 for normal text, 3:1 for large text. Test with Apple's Accessibility Inspector or with the system "Color Filters" simulation.

Avoid information conveyed by color ALONE. A red error state should also have an icon, an exclamation, or text — so colorblind users get the signal.

### The polish dividend

Apps that nail accessibility ALSO feel better to non-disabled users. Larger touch targets = fewer mis-taps. Higher contrast = easier scanning. Reduce Motion alternatives = faster perceived performance. Accessibility = polish.

---

## 20. Liquid Glass (iOS 26)

iOS 26 introduces Liquid Glass — a new translucent, refractive material that responds to motion and content. If you're targeting iOS 26+, this is your primary polish surface.

### The basics

```swift
Button("Action") { }
    .padding()
    .glassEffect() // Default: .regular variant, .capsule shape
```

### Variants

- `.regular` — standard frosted glass with subtle tint
- `.clear` — minimal frosting, mostly transparent
- `.identity` — the "no-op" variant, useful for animation states

### Modifiers chained on `.glassEffect()`

```swift
.glassEffect(.regular.tint(.purple))                // tinted glass
.glassEffect(.regular.tint(.purple.opacity(0.8)))  // see-through tint
.glassEffect(.regular.interactive())                // scales/bounces on tap
```

### `GlassEffectContainer`

When multiple glass surfaces overlap or sit nearby, group them in a `GlassEffectContainer`:
```swift
GlassEffectContainer {
    Button(...) .glassEffect()
    Button(...) .glassEffect()
}
```

The container ensures consistent blur, lighting direction, and refraction across all glass elements within.

### Rules for Liquid Glass

1. **Glass for floating controls only.** Don't make backgrounds glass. The CONTENT shows through glass; if everything is glass, there's nothing to show.
2. **Tint primary actions only.** When everything is tinted, nothing stands out. Pick the one primary action per screen and tint it; leave secondary/tertiary as clear glass.
3. **Interactive variant for tappable elements.** Adds the right amount of bounce and shimmer on tap.
4. **Don't over-apply.** A nav bar that's glass + a tab bar that's glass + a card that's glass = visual mush. Use glass for the ONE floating control layer.
5. **iOS 26 only.** For older OS, fall back to `.thinMaterial` or solid backgrounds.

```swift
@ViewBuilder
func adaptiveBackground() -> some View {
    if #available(iOS 26, *) {
        Color.clear.glassEffect(.regular.interactive())
    } else {
        Color.clear.background(.thinMaterial)
    }
}
```

### Custom shape glass

```swift
.glassEffect(.regular, in: .rect(cornerRadius: 18, style: .continuous))
```

For floating action buttons (FABs) — `in: .circle`. For floating bars — `in: .capsule`.

### What Liquid Glass replaces

- Old: `UIBlurEffect(style: .systemThinMaterial)`
- Old: `.background(.thinMaterial)` (still works, but glass adds refraction + tint)
- Old: hand-tuned shadows + blurs

### Reference

- [Apple — Applying Liquid Glass to custom views](https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views)
- [Donny Wals — Designing custom UI with Liquid Glass](https://www.donnywals.com/designing-custom-ui-with-liquid-glass-on-ios-26/)

---

## 21. The Final 5% checklist

Run this before considering ANY screen done.

### Motion
- [ ] Every tap has a visible press state (scale ~0.97 on touch-down).
- [ ] Every meaningful state change uses a spring (`.spring(duration:bounce:)`).
- [ ] Concurrent animations are staggered by 30–80ms — nothing animates simultaneously unless intentional.
- [ ] Hero transitions use `matchedGeometryEffect` with structural similarity between source and destination.
- [ ] Gesture-driven animations carry velocity (`interpolatingSpring(initialVelocity:)`).
- [ ] Sliders, dials, scrub bars use `.linear` — no springs fighting the finger.
- [ ] Numeric changes use `.contentTransition(.numericText(value:))` + `.monospacedDigit()`.
- [ ] SF Symbol changes use `.contentTransition(.symbolEffect(.replace))`.

### Typography
- [ ] All text uses semantic Dynamic Type styles (`.body`, `.title3`, etc.), not hardcoded sizes.
- [ ] Numbers that change use `.monospacedDigit()`.
- [ ] No `.tracking()` on system text (let SF Pro's automatic tracking do its job).
- [ ] All-caps labels have positive tracking (1.2–2.0pt).
- [ ] Display sizes (28pt+) use `design: .rounded` IF the brand calls for warmth; `.default` if precision.
- [ ] Body text is `.leading`-aligned (never centered).

### Color
- [ ] Backgrounds use semantic system colors, not hardcoded.
- [ ] Foreground hierarchy uses `.primary` / `.secondary` / `.tertiary` / `.quaternary`.
- [ ] Single accent color tints ONE primary action per screen.
- [ ] Shadows are colored (`.black.opacity(0.06–0.18)`), not pure black at full opacity.
- [ ] OLED black (`#000000`) used only in camera/photo/video contexts.

### Haptics
- [ ] Every user-initiated state change has a `.sensoryFeedback` modifier.
- [ ] Haptic intensity matches gesture weight (light for taps, medium for confirms, heavy rare).
- [ ] No haptic spam — selection changes throttled to detents, not every pixel.

### Touch
- [ ] All tap targets ≥ 44 × 44pt via `.contentShape(Rectangle())`.
- [ ] Drag gestures respect rubber-banding at edges.
- [ ] Swipe-to-dismiss has progressive feedback (background darkens, haptic at threshold).

### Loading & empty
- [ ] No spinner under 500ms.
- [ ] Skeletons structurally match the real content.
- [ ] Optimistic UI for every user-initiated mutation.
- [ ] Empty states have illustration + warm copy + clear action.

### Imagery
- [ ] Images cross-fade on load (no instant pop-in).
- [ ] Photo cells have subtle 0.5pt edge stroke for definition.

### Typography of moments
- [ ] Microcopy is brand-voice consistent across every surface.
- [ ] Buttons use action verbs, not bureaucratic words.
- [ ] No "Submit" / "Proceed" / "OK" — replace with specific verbs.

### Accessibility
- [ ] Animations adapt for Reduce Motion.
- [ ] Materials adapt for Reduce Transparency.
- [ ] All interactive icons have descriptive VoiceOver labels (with hints).
- [ ] Tested at largest Dynamic Type without breaking.

### iOS 26 specifically
- [ ] Floating controls use `.glassEffect()` with `.interactive` where appropriate.
- [ ] Only PRIMARY actions are tinted; secondaries stay clear glass.
- [ ] Overlapping glass surfaces grouped in `GlassEffectContainer`.

### Coherence
- [ ] Every screen (settings, paywall, empty state, error, hero) has the same polish level.
- [ ] No "dirty bathroom" — no neglected corner.

### The smile test
- [ ] Someone using the app for 30 seconds visibly enjoys at least one moment.

---

## 22. Anti-patterns

The list of things that signal "this wasn't considered":

1. **`opacity: 0 → 1` modals appearing centered with no spring.** Slide from edge or grow from trigger.
2. **Spinners under 500ms.** If it loads in 200ms, just show the result.
3. **`Toast: "Saved!"`** for important actions. Show the result inline, in context.
4. **"Inter" font.** Reads as web. Use SF Pro.
5. **Purple → blue → pink gradients.** AI cliché. Pick brand colors only.
6. **Hardcoded font sizes (`.font(.system(size: 17))`).** Use Dynamic Type styles.
7. **`.shadow(color: .black, radius: 4)`** with full-opacity pure black. Use 0.06–0.18 opacity.
8. **Custom spinners.** Use `ProgressView()`.
9. **Modals that fade in instead of presenting as sheets.** Use `.sheet` with detents.
10. **Tap targets smaller than 44pt.**
11. **Buttons without press states.**
12. **Bouncy spring on every interaction.** Use bouncy for celebrations only. Use snappy/smooth for the daily 99%.
13. **Hero animations between dissimilar views.** Source and destination must share structure.
14. **Numbers without `.monospacedDigit()`.** They jitter as digits change.
15. **All-caps labels without tracking.** Looks compressed and amateur.
16. **`Submit` as a button label.** What does it submit? Be specific.
17. **Empty states with just text.** "Nothing here" is hostile. Add warmth.
18. **First-launch with no celebration.** The user just installed your app. Acknowledge it.
19. **Settings without sections.** A flat list of toggles is exhausting.
20. **Sheet that doesn't snap to detents.** Set `.presentationDetents([.medium, .large])`.
21. **Hero transitions without staggered body content.** The destination should reveal in waves, not all at once.
22. **Reduce Motion ignored.** Every spring needs a non-spring fallback.
23. **Microcopy that sounds like a system error.** Rewrite in your brand voice.
24. **Identical heights for stacked sheets.** Each layer should be visibly different in size.
25. **Animations that aren't interruptible.** Tapping mid-animation should re-target gracefully.
26. **Haptics on every list scroll.** Vibrating phone = bad app.
27. **`Color.gray.opacity(0.5)` everywhere.** Use `Color(.tertiaryLabel)` or `Color(.systemGray4)` — semantic.
28. **Centered body text in any context.** Body = `.leading`-aligned. Center only display titles and CTAs.
29. **Forgetting Liquid Glass on iOS 26+ apps.** Default `UIBlurEffect` is iOS 18 vintage.
30. **App that works perfectly without showing personality once.** What's the point?

---

## Final principles

Adapted from Family's design philosophy, the Halide team's manifesto, and Linear's craft principles:

1. **You're not making an app. You're making a thing.** Talk about it in those terms. "The camera." "The notebook." "The to-do."
2. **One opinion per decision.** "Should the corner radius be 16 or 18?" Pick one. Apply it everywhere. Defend it.
3. **Polish everything equally.** The settings page = the hero page = the empty state = the paywall = the error screen.
4. **Restraint over volume.** A soft haptic + a 0.2s spring + a perfectly-placed shadow > confetti everywhere.
5. **The user shouldn't NOTICE polish — they should FEEL it.** Specifically: they shouldn't be able to articulate why your app feels different. They should just know.
6. **Test at half-speed.** Record your screen. Play at 0.5×. Look for: things that teleport, animations that fight, simultaneous motions, mismatched curves. Fix them.
7. **Look for "dirty bathrooms".** Walk through every screen of your app. Find the one you're least proud of. Polish it before adding any new features.

The benchmark: A friend uses your app for 30 seconds. They say "this feels nice" without being able to explain why. They mention it to someone else as "that really polished app." They install it on their other devices because it's a *pleasure to use*, not because they need it.

That's the final 5%. That's where products live forever.

---

## Reference reading

The texts every iOS design engineer should have read:

- [Rauno Freiberg — Invisible Details of Interaction Design](https://rauno.me/craft/interaction-design)
- [Rauno Freiberg — interfaces (GitHub)](https://github.com/raunofreiberg/interfaces) — a non-exhaustive list of details
- [Karri Saarinen — 10 Rules for Crafting Products That Stand Out](https://www.figma.com/blog/karri-saarinens-10-rules-for-crafting-products-that-stand-out/)
- [The Linear Method](https://linear.app/method)
- [How we redesigned the Linear UI](https://linear.app/now/how-we-redesigned-the-linear-ui)
- [Behind the Design: Halide Mark II — Apple Developer](https://developer.apple.com/news/?id=x6bv1a36)
- [The Road to Halide Mark III — Lux Camera](https://www.lux.camera/the-road-to-halide-mark-3/)
- [Daring Fireball: Halide review](https://daringfireball.net/2017/05/halide)
- [Family Values — Benji Taylor](https://benji.org/family-values) (the design-with-taste skill's source)
- [Apple — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Apple WWDC22 — Meet the expanded San Francisco font family](https://developer.apple.com/videos/play/wwdc2022/110381/)
- [Apple WWDC20 — The details of UI typography](https://developer.apple.com/videos/play/wwdc2020/10175/)
- [Devouring Details — Rauno Freiberg's interaction design course](https://devouringdetails.com/)
- [Donny Wals — Designing custom UI with Liquid Glass](https://www.donnywals.com/designing-custom-ui-with-liquid-glass-on-ios-26/)
- [SwiftUI Spring Animations — GetStream reference repo](https://github.com/GetStream/swiftui-spring-animations)
- [Apple — Applying Liquid Glass to custom views](https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views)

And the apps to study (install them, observe everything):
- **Halide / Kino** (Lux) — camera polish
- **Things 3** (Cultured Code) — micro-interaction polish
- **Granola** — invisible design + lock-screen integration
- **Apple Music** — hero animations + onboarding
- **Apple Photos** — pinch transitions + matched geometry
- **Lapse** — wait-as-feature, brand polish
- **Linear (iOS)** — craft + opinionated layouts
- **Family** — fluid app feel (study video reviews if not on iOS)
- **Mercury (iOS)** — banking polish
- **Glass** — photography community polish
- **Day One** — journaling polish + animations
- **Slopes** — sports tracker with stunning visualization polish
- **Mela** — recipe app, simple but every detail considered
- **Tot** — Iconfactory's minimalist note tool, master class in restraint
- **Bear** — note-taking, beautiful typography
- **Lex** — writing tool, polish in the smallest details

Read them. Steal from them. Make something better.


---

