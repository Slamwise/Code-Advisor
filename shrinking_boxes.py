import pygame
import sys

# Initialize Pygame
pygame.init()

# Load the image
bg_image = pygame.image.load("D:/repos/Limina/app/test/animations/test.jpg")
screen = pygame.display.set_mode(bg_image.get_rect().size)
pygame.display.set_caption("Bounding Box Animation")

# From predictions To-do: convert to variable
polygons = [
    [[83, 15], [292, 15], [292, 42], [83, 42]], [[83, 70], [911, 68], [912, 89], [83, 90]], [[84, 95], [740, 95], [740, 113], [84, 113]], [[880, 145], [908, 145], [908, 163], [880, 163]], [[101, 148], [355, 148], [355, 167], [101, 167]], [[101, 202], [538, 202], [538, 222], 
    [101, 222]], [[101, 231], [645, 231], [645, 251], [101, 251]], [[101, 259], [822, 259], [822, 278], [101, 278]], [[101, 288], [676, 288], [676, 307], [101, 307]], [[83, 327], [909, 327], [909, 347], [83, 347]], [[83, 352], [506, 352], [506, 371], [83, 371]], [[83, 392], [214, 392], [214, 412], [83, 412]], [[83, 431], [921, 431], [921, 451], [83, 451]], [[83, 456], [907, 455], [907, 474], [83, 476]], [[83, 480], [160, 480], [160, 499], [83, 499]], [[83, 519], [886, 519], [886, 540], [83, 540]], [[83, 544], [204, 544], [204, 564], [83, 564]], [[83, 583], [913, 584], [913, 604], [83, 
    602]], [[83, 609], [378, 609], [378, 627], [83, 627]], [[82, 655], [211, 655], [211, 679], [82, 679]], [[84, 697], [419, 697], [419, 715], [84, 715]], [[883, 747], [907, 747], [907, 764], [883, 764]], [[101, 752], [274, 752], [274, 770], [101, 770]]
    ]

# Calculate the center of the screen
center_x = screen.get_width() / 2
center_y = screen.get_height() / 2

# Animation parameters
animation_time = 60  # Number of frames for the animation

def ease_out_quad(x):
    """Easing function: starts fast, then decelerates."""
    return 1 - (1 - x) * (1 - x)

def animate_bbox(start_frame, bbox, current_frame):
    """Calculate the animated position and size of the bbox with deceleration."""
    if current_frame > start_frame + animation_time:
        return bbox  # Animation complete
    progress = (current_frame - start_frame) / animation_time
    eased_progress = ease_out_quad(progress)  # Apply easing function
    x, y, x2, y2 = bbox
    width, height = x2 - x, y2 - y
    new_width = width * eased_progress
    new_height = height * eased_progress
    new_x = center_x - new_width / 2 + (x - center_x) * eased_progress
    new_y = center_y - new_height / 2 + (y - center_y) * eased_progress
    return (new_x, new_y, new_x + new_width, new_y + new_height)

def animate_point(start_frame, point, current_frame):
    """Calculate the animated position of a point shrinking from screen edges."""
    if current_frame > start_frame + animation_time:
        return point  # Animation complete
    progress = (current_frame - start_frame) / animation_time
    eased_progress = ease_out_quad(progress)  # Apply easing function
    
    x, y = point
    
    # Determine the closest edges
    closest_x = 0 if (x - center_x) < 0 else screen.get_width()
    closest_y = 0 if (y - center_y) < 0 else screen.get_height()
    
    # Calculate the new position
    new_x = closest_x + (x - closest_x) * eased_progress
    new_y = closest_y + (y - closest_y) * eased_progress
    
    return (new_x, new_y)

def animate_polygon(start_frame, polygon, current_frame):
    """Animate a polygon from edges to final shape."""
    return [animate_point(start_frame, point, current_frame) for point in polygon]

# ... rest of your code ...


def animate_polygon(start_frame, polygon, current_frame):
    """Animate a polygon."""
    return [animate_point(start_frame, point, current_frame) for point in polygon]

# Main loop
clock = pygame.time.Clock()
frame_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Restart animation on click
            frame_count = 0

    # Draw the background
    screen.blit(bg_image, (0, 0))

    # Draw each polygon
    for i, polygon in enumerate(polygons):
        animated_polygon = animate_polygon(i * 10, polygon, frame_count)
        pygame.draw.polygon(screen, (0, 225, 0), animated_polygon, 2)

    pygame.display.flip()
    frame_count += 5
    clock.tick(20)  # FPS

    save_video = False
    if save_video == True:
        import os
        # Directory to save frames
        frame_directory = "./frames"
        os.makedirs(frame_directory, exist_ok=True)
        # Save the frame
        frame_index = int(frame_count)
        frame_filename = os.path.join(frame_directory, f"frame_{frame_index:04d}.jpeg")
        pygame.image.save(screen, frame_filename)
        frame_count += 1.5
