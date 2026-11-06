import nltk
from nltk.chat.util import Chat, reflections

personal_dataset = [
    [r"Hi",["Hello"]],
    [r"(?i).*who are you.*|.*tell me about yourself.*",["I am BS AI student at Superior University"]],
    [r"(?i).*what is your name.*",["My Name is Moiz Safdar"]],
    [r"(?i).*how old are you.*|.*your age.*",["I am 20 year Old"]],
    [r"(?i).*what are your interests.*|.*hobbies.*",["My interest include graphic designing and weigthlifting. Ive been doing them for quite some time now"]],
    [r"(?i).*where are you from.*|.*your hometown.*", ["I am from Lahore,Pakistan."]],
    [r"(?i).*what is your daily routine.*",["My daily routine mainly includes going university, studying, and fitness."]],
    [r"(?i).*what is your favorite sport.*|.*what kind of sports are u into.*",["I enjoy fitness activities, especially weightlifting and sometimes badminton .","Weightlifting is one of my favorite physical activities."]],
    [r"(?i).*how long have you been weightlifting.*",["I have been into weightlifting for 1.5 year."]],
    [r"(?i).*why do you choose weightlifting.*",["I chose weightlifting because it helps me improve my strength and discipline."]],
    [r"(?i).*what are your strengths.*",["My strengths include creativity, problem-solving, and consistency.","I consider creativity, consistency, and adaptability as my strengths."]],
    [r"(?i).*where do you study.*|.*which university.*",["I am currently in Superior University","I am Student At Superior University"]],
    [r"(?i).*what is your degree.*|.*what program did u take.*",["I am studying BS Aritficial Intelligence","My degree program is Bachelor of Science in Artificial Intelligence."]],
    [r"(?i).*what semester.*|.*which semester.*",["halfway through my 3rd semester "]],
    [r"(?i).*why did u choose BSAI.*|.*why artificial intelligence.*",["As a Graphic Designer I used to use Ai so i got more curious how AI works so I decide to choose it my Self."]],
    [r"(?i).*what are your expectations from university life.*",["I expect to gain knowledge and develop professional skills"]],
    [r"(?i).*what is your favorite subject.*", ["I am particularly interested in Artificial Intelligence","Artificial Intelligence are among my favorite subjects."]],
    [r"(?i).*what are your skills.*|.*technical skills.*.",["My skills include HTML, CSS , Python , C++, graphic designing, and video editing."]],
    [r"(?i).*programming languages.*",["I have experience with Python, C++"]],
    [r"(?i).*Graphic Designing.*",["I've been doing Graphic Designing for 3-4 years, I have good desiging skills and experince with Photoshop "]],
    [r"(?i).*what is your favorite tool for designing.*", ["Adobe Photoshop is my preferred tool for graphic designing."]],
    [r"(?i).*what software do you use.*", ["I use Adobe Photoshop, Adobe Premiere Pro, CapCut, and programming tools for my work."]], 
    [r"(?i).*Video Editing.*",["I have Good Experience with Adobe Premiere Pro and Capcut"]],
    [r"(?i).*what kind of designs do you create.*",["I create social media posts, promotional graphics, and creative designs", "I work on different graphic designing projects, including digital and social media designs."]],
    [r"(?i).*how did you learn graphic designing.*",["I learned it from my father and developed my designing skills through regular practice and experience.","I learned graphic designing from my father and practiced it alot "]],
    [r"(?i).*do you work on projects.*",["Yes, I work on academic and personal projects to improve my skills."]],
    [r"(?i).*what projects have you worked on.*",["I have worked on programming, web development, and university projects."]],
    [r"(?i).*what is your experience with web development.*|.*How much do you know about web development.*",["I have experience with HTML and CSS and basic web development."]],
    [r"(?i).*what do you know about artificial intelligence.*|.*what is artificial intelligence.*",["Artificial Intelligence enables machines to try to think and work like humans."]],
    [r"(?i).*do you prefer working alone or in a team.*",["I am comfortable when I am working alone."]],
    [r"(?i).*are you interested in freelancing.*",["Yes, I am interested in freelancing to gain experience and learn.","I would like to try freelancing and work with different clients."]],
    ]

personal_bot = Chat(personal_dataset, reflections)
def personal_chatbot():
  print("Chatbot: Welcome to My Personal chatbot")
  while True:
    user_input = input("You: ")
    if user_input.lower() != 'exit':
      print("Chatbot:",personal_bot.respond(user_input) or "I dont know the answer" )
    else:
      print("Chatbot: GoodBye!")
      break

personal_chatbot()