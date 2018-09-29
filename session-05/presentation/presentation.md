# Session #5

---

##  First App
https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/index.html
![inline, 50%](app.png)
---



---

## Build a Basic UI

- Create a project in Xcode
- Identify the purpose of key files that are created with an Xcode project template
- Open and switch between files in a project
- Run an app in iOS Simulator
- Add, move, and resize UI elements in a storyboard



---
## Build a Basic UI ...

- Edit the attributes of UI elements in a storyboard using the Attributes inspector
- View and rearrange UI elements using the outline view
- Preview a storyboard UI using the Assistant editor’s Preview mode
- Use Auto Layout to lay out a UI that automatically adapts to the user’s device size


---
## Connect the UI to Code

- Explain the relationship between a scene in a storyboard and the underlying view controller
- Create outlet and action connections between UI elements in a storyboard and source code
- Process user input from a text field and display the result in the UI
- Make a class conform to a protocol

---

## Connect the UI to Code ...

- Understand the delegation pattern
- Follow the target-action pattern when designing app architecture


---

## What is a View Controller

- Manage a single content view with its hierarchy of subviews
- Coordinate the flow of information between the app’s data model and the views that display that data
- Manage the life cycle of their content views
- Handle orientation changes when the device is rotated
- Define the navigation within your app
- Implement the behavior to respond to user input

---

## Target-Action pattern

- The event is the user tapping the Set Default Text button.
- The action is `setDefaultLabelText(_)`.
- The target is `ViewController` (where the action method is defined).
- The sender is the Set Default Label Text button.

---

## Delegation

A delegate is an object that acts on behalf of, or in coordination with, another object. 
Any object can serve as a delegate for another object as long as it *conforms* to the appropriate *protocol*.
