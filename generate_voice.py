import asyncio
from pathlib import Path
import edge_tts

# Male English neural voice. Alternatives:
# "en-GB-RyanNeural" (British male)
# "en-US-ChristopherNeural" (American male)
VOICE = "en-US-GuyNeural"
RATE = "-10%"
OUT = Path("audio")
OUT.mkdir(exist_ok=True)

NARRATION = [
    """Imagine a triangle drawn on a coordinate plane. Now imagine that it can slide to a new position, turn around a point, flip like a mirror image, or grow larger while keeping the same shape. These changes are called mathematical transformations. Transformations are rules that move points from one position to another. They help us describe movement precisely, using coordinates, angles, and scale factors. In this lesson, we will explore four important transformations: translation, rotation, reflection, and dilation. As we go, watch how the triangle changes, and notice which properties stay the same.""",

    """A geometric transformation takes an original figure and produces an image of that figure. We often call the original shape the preimage and the new shape the image. Each point on the preimage has a matching point on the image. We can name matching vertices with letters, such as A and A-prime, B and B-prime, and C and C-prime. A transformation can change a figure's position, direction, or size. Some transformations preserve both shape and size; these are called rigid transformations. Translation, rotation, and reflection are rigid transformations. Dilation changes size, but it preserves shape and angles.""",

    """First, let's look at translation. Translation is a slide. Every point moves the same distance in the same direction. The figure does not turn, flip, or change size. On a coordinate plane, a translation can be written as x comma y maps to x plus a, comma y plus b. The value a tells us how far to move horizontally, and b tells us how far to move vertically. For example, the rule x plus three, y plus two moves every point three units right and two units up. If point A is at one, one, its image A-prime is at four, three. The side lengths and angles stay exactly the same.""",

    """Next is rotation. A rotation turns a figure around a fixed point called the centre of rotation. We measure the turn in degrees. A quarter-turn is ninety degrees, a half-turn is one hundred and eighty degrees, and a full turn is three hundred and sixty degrees. When we rotate a point around the origin by ninety degrees counterclockwise, the coordinate rule is x comma y maps to negative y, comma x. For example, the point two, one moves to negative one, two. The triangle changes direction, but its side lengths, angles, and overall size remain unchanged. The centre stays fixed while the other points travel around it.""",

    """Now imagine holding a shape in front of a mirror. The flipped image is called a reflection. The line that acts like the mirror is called the line of reflection. A reflection across the x-axis changes the sign of the y-coordinate: x comma y maps to x comma negative y. A reflection across the y-axis changes the sign of the x-coordinate: x comma y maps to negative x comma y. Points on the mirror line do not move. Reflections preserve distances and angle measures, but they reverse orientation. That is why a reflected shape looks like a mirror image rather than simply a turned copy.""",

    """Our final transformation is dilation. Dilation enlarges or reduces a figure from a fixed centre by a scale factor. If the centre is the origin and the scale factor is k, the coordinate rule is x comma y maps to kx comma ky. When k is greater than one, the image becomes larger. When k is between zero and one, the image becomes smaller. For example, a scale factor of two doubles every distance from the centre. A scale factor of one half reduces those distances to half. Dilation preserves angle measures and shape, so the image is similar to the original, but its side lengths change. We see transformations in maps, architecture, animation, design, robotics, and computer graphics.""",

    """Let's review the four transformations. Translation slides a figure without turning it. Rotation turns a figure around a centre. Reflection flips a figure across a mirror line. Dilation enlarges or reduces a figure using a scale factor. Translation, rotation, and reflection preserve lengths and angles, while dilation preserves angles and proportional side lengths. These ideas are used in maps, architecture, animation, design, robotics, and computer graphics. The next time you see an object move, turn, flip, or resize, think about the mathematical rule behind it. Thanks for watching, and keep exploring mathematics!"""
]

async def make_clip(index: int, text: str):
    output = OUT / f"scene_{index:02d}.mp3"
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(str(output))
    print(f"Created {output}")

async def main():
    for i, paragraph in enumerate(NARRATION, start=1):
        await make_clip(i, paragraph)
    print(f"\\nAll voice clips created using {VOICE}.")

if __name__ == "__main__":
    asyncio.run(main())
