import os
import django
import sys
from pathlib import Path

# Add the project root directory to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'afro_renaissance.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils.text import slugify
from manifesto.models import ManifestoSection, KeyPoint
from blog.models import Category
from social.models import Profile

def create_superuser():
    """Create a superuser for initial admin access"""
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'AfroRenaissance2024!')
    
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_superuser(username, email, password)
        Profile.objects.create(user=user)
        print(f"Created superuser '{username}' with profile")

def create_manifesto_sections():
    """Create the manifesto sections from the provided text"""
    sections = [
        {
            'title': 'Preamble',
            'content': """Africa stands at the dawn of a new era—an Afro-Renaissance—a transformative movement for economic and social rebirth powered by the talents of our people. Just as the great renaissances of history ignited new ages of discovery and progress, the Afro-Renaissance is our generation's call to unlock Africa's full potential through skill mastery, education, and knowledge empowerment. This manifesto articulates our mission and vision, inspires mass participation, and lays out a clear roadmap for the next five years. We present this as a blueprint for immediate and sustained action—a reference point for policymakers, activists, and every African who dares to dream of a prosperous, self-reliant continent. The urgency is real, the mission is clear: Africa's rebirth must be forged by the hands and minds of its own people, now or never.""",
            'order': 1
        },
        {
            'title': 'Mission',
            'content': """The Afro-Renaissance is a pan-African movement dedicated to unleashing the power of human capital as the catalyst for Africa's economic and social transformation. Its mission is to cultivate a generation of highly skilled, knowledgeable Africans who will drive innovation, build thriving industries, and uplift communities. We seek to master skills and knowledge in every field – from technology and engineering to finance, healthcare, agriculture, and the arts – to break the shackles of dependency and set Africa on a path of self-determined growth. By investing in our people's talents and education, the Afro-Renaissance strives to turn Africa's "brain drain" into "brain gain," empowering citizens to become creators of wealth, solutions, and knowledge.""",
            'order': 2
        },
        {
            'title': 'Vision',
            'content': """Our vision is an Africa reborn as a global center of excellence and opportunity – "a continent of innovators and producers" renowned for its skilled workforce, cutting-edge enterprises, and vibrant knowledge economy.""",
            'order': 3
        },
        {
            'title': 'The Urgency of Now',
            'content': """The call to action cannot wait. Africa is the world's youngest continent, with over 60% of our population under the age of 25. By 2050, Africa's population will nearly double to 2.5 billion. This demographic surge presents a historic opportunity – or a ticking time bomb.""",
            'order': 4
        },
        {
            'title': 'Five-Year Roadmap',
            'content': """Words alone are not enough. The Afro-Renaissance movement outlines a clear, actionable 5-year roadmap broken into three phases. This roadmap is ambitious yet achievable, designed to build momentum year by year – from awareness, to widespread skill acquisition, to tangible economic change.""",
            'order': 5
        }
    ]

    for section_data in sections:
        section, created = ManifestoSection.objects.get_or_create(
            title=section_data['title'],
            defaults={
                'content': section_data['content'],
                'order': section_data['order'],
                'slug': slugify(section_data['title'])
            }
        )
        if created:
            print(f"Created manifesto section: {section.title}")

def create_key_points():
    """Create key points for the manifesto"""
    points = [
        {
            'title': 'Education First',
            'description': 'Prioritizing education and skill development as the foundation of Africa\'s transformation',
            'icon': 'fa-graduation-cap',
            'section': 'Mission'
        },
        {
            'title': 'Innovation Hub',
            'description': 'Transforming Africa into a global center for innovation and technological advancement',
            'icon': 'fa-lightbulb',
            'section': 'Vision'
        },
        {
            'title': 'Economic Growth',
            'description': 'Building sustainable industries and creating opportunities for economic prosperity',
            'icon': 'fa-chart-line',
            'section': 'Vision'
        },
        {
            'title': 'Unity in Action',
            'description': 'Fostering collaboration across borders and communities for collective progress',
            'icon': 'fa-hands-helping',
            'section': 'Vision'
        }
    ]

    for point_data in points:
        section = ManifestoSection.objects.get(title=point_data['section'])
        point, created = KeyPoint.objects.get_or_create(
            title=point_data['title'],
            defaults={
                'description': point_data['description'],
                'icon': point_data['icon'],
                'section': section
            }
        )
        if created:
            print(f"Created key point: {point.title}")

def create_blog_categories():
    """Create initial blog categories"""
    categories = [
        'Education & Skills',
        'Innovation & Technology',
        'Economic Development',
        'Culture & Arts',
        'Youth Empowerment',
        'Policy & Governance'
    ]

    for category_name in categories:
        category, created = Category.objects.get_or_create(
            name=category_name,
            defaults={'slug': slugify(category_name)}
        )
        if created:
            print(f"Created blog category: {category.name}")

def main():
    """Main function to initialize all data"""
    print("Initializing database with initial data...")
    
    create_superuser()
    create_manifesto_sections()
    create_key_points()
    create_blog_categories()
    
    print("Database initialization completed successfully!")

if __name__ == '__main__':
    main()