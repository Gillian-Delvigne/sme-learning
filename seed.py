import uuid
from datetime import datetime
from models import (
    Base,
    Role,
    Skill,
    Course,
    Employee,
    Enrollment,
    EnrollmentStatus,
    Activity,
    ActivityType,
    Question,
    Answer,
)
from db import engine, SessionLocal

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with SessionLocal() as session:
    # --- Roles ---
    r1 = Role(id=uuid.uuid4(), title="Software Developer")
    r2 = Role(id=uuid.uuid4(), title="Lead Developer")
    r3 = Role(id=uuid.uuid4(), title="Product Owner")
    r4 = Role(id=uuid.uuid4(), title="DevOps Engineer")
    r5 = Role(id=uuid.uuid4(), title="Product Manager")
    r6 = Role(id=uuid.uuid4(), title="Community Manager")
    r7 = Role(id=uuid.uuid4(), title="Marketing Manager")
    r8 = Role(id=uuid.uuid4(), title="Sales Representative")
    r9 = Role(id=uuid.uuid4(), title="HR Manager")
    r10 = Role(id=uuid.uuid4(), title="Data Analyst")
    r11 = Role(id=uuid.uuid4(), title="Customer Support")
    session.add_all([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11])
    session.commit()

    # --- Skills ---
    # Tech
    sk1 = Skill(
        id=uuid.uuid4(),
        name="Python",
        description="Object-oriented programming and scripting with Python",
    )
    sk2 = Skill(
        id=uuid.uuid4(),
        name="JavaScript",
        description="Frontend and backend development with JS/TypeScript",
    )
    sk3 = Skill(
        id=uuid.uuid4(),
        name="SQL",
        description="Relational database modeling and querying",
    )
    sk4 = Skill(
        id=uuid.uuid4(),
        name="Git",
        description="Version control and collaborative workflows with Git",
    )
    sk5 = Skill(
        id=uuid.uuid4(),
        name="Docker",
        description="Application containerization with Docker and Compose",
    )
    sk6 = Skill(
        id=uuid.uuid4(),
        name="CI/CD",
        description="Building and maintaining continuous integration and deployment pipelines",
    )
    sk7 = Skill(
        id=uuid.uuid4(),
        name="REST API",
        description="Designing and consuming RESTful APIs",
    )
    sk8 = Skill(
        id=uuid.uuid4(),
        name="Linux",
        description="Linux system administration and Bash scripting",
    )
    sk9 = Skill(
        id=uuid.uuid4(),
        name="Agile/Scrum",
        description="Agile methodology and Scrum practices for project delivery",
    )
    sk10 = Skill(
        id=uuid.uuid4(),
        name="Product Management",
        description="Roadmap definition and product backlog management",
    )
    sk11 = Skill(
        id=uuid.uuid4(),
        name="User Stories",
        description="Writing and prioritizing user stories and acceptance criteria",
    )
    sk12 = Skill(
        id=uuid.uuid4(),
        name="Technical Leadership",
        description="Software architecture decisions and team code review",
    )
    # Non-tech
    sk13 = Skill(
        id=uuid.uuid4(),
        name="Social Media",
        description="Managing and growing brand presence across social media platforms",
    )
    sk14 = Skill(
        id=uuid.uuid4(),
        name="Content Creation",
        description="Writing, editing and publishing engaging content for various channels",
    )
    sk15 = Skill(
        id=uuid.uuid4(),
        name="SEO/SEM",
        description="Optimizing content for search engines and managing paid campaigns",
    )
    sk16 = Skill(
        id=uuid.uuid4(),
        name="CRM Tools",
        description="Using customer relationship management software to track leads and clients",
    )
    sk17 = Skill(
        id=uuid.uuid4(),
        name="Copywriting",
        description="Crafting persuasive and clear marketing or sales copy",
    )
    sk18 = Skill(
        id=uuid.uuid4(),
        name="Data Analysis",
        description="Interpreting datasets to extract business insights using tools like Excel or Python",
    )
    sk19 = Skill(
        id=uuid.uuid4(),
        name="Project Management",
        description="Planning, executing and monitoring projects to meet deadlines and budgets",
    )
    sk20 = Skill(
        id=uuid.uuid4(),
        name="Recruitment",
        description="Sourcing, interviewing and onboarding new talent",
    )
    sk21 = Skill(
        id=uuid.uuid4(),
        name="Customer Support",
        description="Handling client requests, complaints and escalations effectively",
    )
    sk22 = Skill(
        id=uuid.uuid4(),
        name="Public Speaking",
        description="Presenting ideas clearly to diverse audiences in professional settings",
    )
    session.add_all(
        [
            sk1,
            sk2,
            sk3,
            sk4,
            sk5,
            sk6,
            sk7,
            sk8,
            sk9,
            sk10,
            sk11,
            sk12,
            sk13,
            sk14,
            sk15,
            sk16,
            sk17,
            sk18,
            sk19,
            sk20,
            sk21,
            sk22,
        ]
    )
    session.commit()

    # --- Courses ---
    c1 = Course(
        id=uuid.uuid4(),
        title="Git Basics",
        description="Learn version control fundamentals and collaborative Git workflows",
        theme="Tech",
    )
    c2 = Course(
        id=uuid.uuid4(),
        title="Python Fundamentals",
        description="Core Python programming: syntax, data structures, OOP and scripting",
        theme="Tech",
    )
    c3 = Course(
        id=uuid.uuid4(),
        title="SQL & Databases",
        description="Relational database design, SQL queries, joins and indexing",
        theme="Tech",
    )
    c4 = Course(
        id=uuid.uuid4(),
        title="Docker & Containers",
        description="Containerization principles, Dockerfile authoring and Docker Compose",
        theme="Tech",
    )
    c5 = Course(
        id=uuid.uuid4(),
        title="REST API Development",
        description="Design and build RESTful APIs with authentication and documentation",
        theme="Tech",
    )
    c6 = Course(
        id=uuid.uuid4(),
        title="CI/CD Pipelines",
        description="Automate build, test and deployment workflows with GitHub Actions",
        theme="Tech",
        validity_months=12,
    )
    c7 = Course(
        id=uuid.uuid4(),
        title="Data Analysis Fundamentals",
        description="Explore and visualize datasets using Python and SQL",
        theme="Tech",
    )
    c8 = Course(
        id=uuid.uuid4(),
        title="Agile & Scrum",
        description="Agile principles, Scrum ceremonies, roles and backlog management",
        theme="Management",
        validity_months=24,
    )
    c9 = Course(
        id=uuid.uuid4(),
        title="GDPR & Data Privacy",
        description="EU data protection regulations, compliance obligations and best practices",
        theme="Compliance",
        validity_months=12,
    )
    c10 = Course(
        id=uuid.uuid4(),
        title="Copywriting",
        description="Write clear, persuasive and audience-focused copy for business contexts",
        theme="Marketing",
    )
    c11 = Course(
        id=uuid.uuid4(),
        title="Content Creation Strategy",
        description="Plan and produce multi-channel content aligned with business goals",
        theme="Marketing",
    )
    c12 = Course(
        id=uuid.uuid4(),
        title="Social Media Strategy",
        description="Build and manage brand presence across social platforms with data-driven tactics",
        theme="Marketing",
    )
    c13 = Course(
        id=uuid.uuid4(),
        title="Customer Relations",
        description="Handle client interactions, complaints and escalations with empathy and efficiency",
        theme="Support",
    )
    session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13])
    session.commit()

    # --- Course prerequisites ---
    c5.prerequisites.extend([c2, c3])  # REST API <-- Python + SQL
    c6.prerequisites.extend([c1, c4])  # CI/CD <-- Git + Docker
    c7.prerequisites.append(c3)  # Data Analysis <-- SQL
    c11.prerequisites.append(c10)  # Content Creation <-- Copywriting
    c12.prerequisites.append(c11)  # Social Media <-- Content Creation
    session.commit()

    # --- Employees ---
    e1 = Employee(
        id=uuid.uuid4(),
        first_name="Ada",
        last_name="Lovelace",
        role=r1,
    )
    e2 = Employee(
        id=uuid.uuid4(),
        first_name="Bill",
        last_name="Gates",
        role=r1,
    )
    e3 = Employee(
        id=uuid.uuid4(),
        first_name="Dennis",
        last_name="Ritchie",
        role=r1,
    )
    e4 = Employee(
        id=uuid.uuid4(),
        first_name="Grace",
        last_name="Hopper",
        role=r1,
    )
    e5 = Employee(
        id=uuid.uuid4(),
        first_name="Kenneth",
        last_name="Thompson",
        role=r2,
    )
    e6 = Employee(
        id=uuid.uuid4(),
        first_name="Edsger",
        last_name="Dijkstra",
        role=r2,
    )
    e7 = Employee(
        id=uuid.uuid4(),
        first_name="Linus",
        last_name="Torvalds",
        role=r4,
    )
    e8 = Employee(
        id=uuid.uuid4(),
        first_name="Alan",
        last_name="Turing",
        role=r4,
    )
    e9 = Employee(
        id=uuid.uuid4(),
        first_name="Steve",
        last_name="Jobs",
        role=r3,
    )
    e10 = Employee(
        id=uuid.uuid4(),
        first_name="Marissa",
        last_name="Mayer",
        role=r5,
    )
    e11 = Employee(
        id=uuid.uuid4(),
        first_name="Florence",
        last_name="Nightingale",
        role=r10,
    )
    e12 = Employee(
        id=uuid.uuid4(),
        first_name="Jimmy",
        last_name="Wales",
        role=r6,
    )
    e13 = Employee(
        id=uuid.uuid4(),
        first_name="Seth",
        last_name="Godin",
        role=r7,
    )
    e14 = Employee(
        id=uuid.uuid4(),
        first_name="Zig",
        last_name="Ziglar",
        role=r8,
    )
    e15 = Employee(
        id=uuid.uuid4(),
        first_name="Tony",
        last_name="Hsieh",
        role=r11,
    )
    e16 = Employee(
        id=uuid.uuid4(),
        first_name="Dave",
        last_name="Ulrich",
        role=r9,
    )
    session.add_all(
        [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16]
    )
    session.commit()

    # --- Activities ---
    # c1 - Git Basics
    a1 = Activity(
        id=uuid.uuid4(),
        title="What is Version Control?",
        type=ActivityType.TEXT,
        sequence=1,
        content="Version control tracks file changes over time, allowing teams to collaborate, review history, and roll back mistakes. Git is the most widely used distributed version control system.",
        pass_threshold=0,
        course=c1,
    )
    a2 = Activity(
        id=uuid.uuid4(),
        title="Git Basics Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c1,
    )
    # c2 - Python Fundamentals
    a3 = Activity(
        id=uuid.uuid4(),
        title="Python: Variables and Data Types",
        type=ActivityType.TEXT,
        sequence=1,
        content="Python is a dynamically typed language. Variables store references to objects, and core types include int, float, str, list, dict, tuple and bool. Understanding mutability and scope is essential for clean Python code.",
        pass_threshold=0,
        course=c2,
    )
    a4 = Activity(
        id=uuid.uuid4(),
        title="Python OOP in 10 minutes",
        type=ActivityType.MEDIA,
        sequence=2,
        content="https://example.com/media/python-oop-intro",
        pass_threshold=0,
        course=c2,
    )
    a5 = Activity(
        id=uuid.uuid4(),
        title="Python Core Concepts Quiz",
        type=ActivityType.QUIZZ,
        sequence=3,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c2,
    )
    # c3 - SQL & Databases
    a6 = Activity(
        id=uuid.uuid4(),
        title="Relational Model Introduction",
        type=ActivityType.TEXT,
        sequence=1,
        content="Relational databases organize data into tables with rows and columns. Each table has a primary key and can reference others via foreign keys. Constraints ensure data integrity across relationships.",
        pass_threshold=0,
        course=c3,
    )
    a7 = Activity(
        id=uuid.uuid4(),
        title="SQL Queries Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c3,
    )
    # c4 - Docker & Containers
    a8 = Activity(
        id=uuid.uuid4(),
        title="Docker in 5 minutes",
        type=ActivityType.MEDIA,
        sequence=1,
        content="https://example.com/media/docker-intro",
        pass_threshold=0,
        course=c4,
    )
    a9 = Activity(
        id=uuid.uuid4(),
        title="Containers & Images Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c4,
    )
    # c5 - REST API Development
    a10 = Activity(
        id=uuid.uuid4(),
        title="REST Principles and HTTP Methods",
        type=ActivityType.TEXT,
        sequence=1,
        content="REST (Representational State Transfer) is an architectural style for APIs. Key principles include statelessness and resource-based URLs. Standard HTTP methods: GET (read), POST (create), PUT/PATCH (update), DELETE (remove).",
        pass_threshold=0,
        course=c5,
    )
    a11 = Activity(
        id=uuid.uuid4(),
        title="Building Your First API",
        type=ActivityType.MEDIA,
        sequence=2,
        content="https://example.com/media/rest-api-demo",
        pass_threshold=0,
        course=c5,
    )
    a12 = Activity(
        id=uuid.uuid4(),
        title="REST API Design Quiz",
        type=ActivityType.QUIZZ,
        sequence=3,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c5,
    )
    # c6 - CI/CD Pipelines
    a13 = Activity(
        id=uuid.uuid4(),
        title="CI/CD Principles",
        type=ActivityType.TEXT,
        sequence=1,
        content="Continuous Integration means merging code frequently and validating it with automated tests. Continuous Delivery extends this by automating releases. CI/CD pipelines reduce integration risk and accelerate feedback loops.",
        pass_threshold=0,
        course=c6,
    )
    a14 = Activity(
        id=uuid.uuid4(),
        title="Pipeline Concepts Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c6,
    )
    # c7 - Data Analysis Fundamentals
    a15 = Activity(
        id=uuid.uuid4(),
        title="Introduction to Data Analysis",
        type=ActivityType.TEXT,
        sequence=1,
        content="Data analysis transforms raw data into insights. The process includes collection, cleaning, exploration, visualization and interpretation. Key tools include Python (pandas, matplotlib) and SQL for structured datasets.",
        pass_threshold=0,
        course=c7,
    )
    a16 = Activity(
        id=uuid.uuid4(),
        title="Pandas & Matplotlib Overview",
        type=ActivityType.MEDIA,
        sequence=2,
        content="https://example.com/media/pandas-matplotlib",
        pass_threshold=0,
        course=c7,
    )
    a17 = Activity(
        id=uuid.uuid4(),
        title="Data Analysis Concepts Quiz",
        type=ActivityType.QUIZZ,
        sequence=3,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c7,
    )
    # c8 - Agile & Scrum
    a18 = Activity(
        id=uuid.uuid4(),
        title="Agile Manifesto Overview",
        type=ActivityType.TEXT,
        sequence=1,
        content="The Agile Manifesto (2001) values individuals over processes, working software over documentation, customer collaboration over contract negotiation, and responding to change over following a plan.",
        pass_threshold=0,
        course=c8,
    )
    a19 = Activity(
        id=uuid.uuid4(),
        title="Scrum Ceremonies Explained",
        type=ActivityType.MEDIA,
        sequence=2,
        content="https://example.com/media/scrum-ceremonies",
        pass_threshold=0,
        course=c8,
    )
    a20 = Activity(
        id=uuid.uuid4(),
        title="Scrum Roles & Events Quiz",
        type=ActivityType.QUIZZ,
        sequence=3,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c8,
    )
    # c9 - GDPR & Data Privacy
    a21 = Activity(
        id=uuid.uuid4(),
        title="Key GDPR Principles",
        type=ActivityType.TEXT,
        sequence=1,
        content="The GDPR establishes six principles: lawfulness, purpose limitation, data minimisation, accuracy, storage limitation, and integrity. Organizations must document their legal basis for processing personal data.",
        pass_threshold=0,
        course=c9,
    )
    a22 = Activity(
        id=uuid.uuid4(),
        title="GDPR Compliance Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c9,
    )
    # c10 - Copywriting
    a23 = Activity(
        id=uuid.uuid4(),
        title="Writing Headlines That Convert",
        type=ActivityType.TEXT,
        sequence=1,
        content="Effective headlines are specific, benefit-driven and audience-focused. Techniques include using numbers, power words and addressing a pain point directly. Avoid vague claims and jargon.",
        pass_threshold=0,
        course=c10,
    )
    a24 = Activity(
        id=uuid.uuid4(),
        title="Copywriting Fundamentals Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c10,
    )
    # c11 - Content Creation Strategy
    a25 = Activity(
        id=uuid.uuid4(),
        title="Content Strategy Fundamentals",
        type=ActivityType.TEXT,
        sequence=1,
        content="A content strategy defines what to create, for whom, on which channels and with what goals. It aligns editorial decisions with business objectives through personas, content pillars and editorial calendars.",
        pass_threshold=0,
        course=c11,
    )
    a26 = Activity(
        id=uuid.uuid4(),
        title="Multi-Channel Content Planning",
        type=ActivityType.MEDIA,
        sequence=2,
        content="https://example.com/media/content-planning",
        pass_threshold=0,
        course=c11,
    )
    a27 = Activity(
        id=uuid.uuid4(),
        title="Content Strategy Quiz",
        type=ActivityType.QUIZZ,
        sequence=3,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c11,
    )
    # c12 - Social Media Strategy
    a28 = Activity(
        id=uuid.uuid4(),
        title="Building a Content Calendar",
        type=ActivityType.MEDIA,
        sequence=1,
        content="https://example.com/media/content-calendar",
        pass_threshold=0,
        course=c12,
    )
    a29 = Activity(
        id=uuid.uuid4(),
        title="Social Media KPIs Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c12,
    )
    # c13 - Customer Relations
    a30 = Activity(
        id=uuid.uuid4(),
        title="Handling Difficult Clients",
        type=ActivityType.TEXT,
        sequence=1,
        content="Effective client relations rely on active listening, empathy and clear communication. When handling complaints, acknowledge the issue first, avoid defensive language, propose a resolution and follow up.",
        pass_threshold=0,
        course=c13,
    )
    a31 = Activity(
        id=uuid.uuid4(),
        title="Customer Service Scenarios Quiz",
        type=ActivityType.QUIZZ,
        sequence=2,
        content="Answer the following questions to validate your understanding. A score of 70% or higher is required.",
        pass_threshold=70,
        course=c13,
    )
    session.add_all(
        [
            a1,
            a2,
            a3,
            a4,
            a5,
            a6,
            a7,
            a8,
            a9,
            a10,
            a11,
            a12,
            a13,
            a14,
            a15,
            a16,
            a17,
            a18,
            a19,
            a20,
            a21,
            a22,
            a23,
            a24,
            a25,
            a26,
            a27,
            a28,
            a29,
            a30,
            a31,
        ]
    )
    session.commit()

    # --- Questions ---
    q1 = Question(
        id=uuid.uuid4(),
        statement="What command initializes a new Git repository?",
        activity=a2,
    )
    q2 = Question(
        id=uuid.uuid4(),
        statement="Which command stages all modified files for commit?",
        activity=a2,
    )
    q3 = Question(
        id=uuid.uuid4(),
        statement="Which of the following is a mutable data type in Python?",
        activity=a5,
    )
    q4 = Question(
        id=uuid.uuid4(),
        statement="What does the `__init__` method define in a Python class?",
        activity=a5,
    )
    q5 = Question(
        id=uuid.uuid4(),
        statement="Which SQL clause filters rows after grouping?",
        activity=a7,
    )
    q6 = Question(
        id=uuid.uuid4(),
        statement="What type of join returns all rows from both tables, including non-matching rows?",
        activity=a7,
    )
    q7 = Question(id=uuid.uuid4(), statement="What is a Docker image?", activity=a9)
    q8 = Question(
        id=uuid.uuid4(),
        statement="Which file defines the instructions to build a Docker image?",
        activity=a9,
    )
    q9 = Question(
        id=uuid.uuid4(),
        statement="Which HTTP method is used to partially update a resource?",
        activity=a12,
    )
    q10 = Question(
        id=uuid.uuid4(),
        statement="What HTTP status code indicates a successfully created resource?",
        activity=a12,
    )
    q11 = Question(
        id=uuid.uuid4(), statement="What does CI stand for in CI/CD?", activity=a14
    )
    q12 = Question(
        id=uuid.uuid4(),
        statement="Which event typically triggers a CI pipeline in a Git-based workflow?",
        activity=a14,
    )
    q13 = Question(
        id=uuid.uuid4(),
        statement="Which pandas method displays a summary of a DataFrame's structure and data types?",
        activity=a17,
    )
    q14 = Question(
        id=uuid.uuid4(), statement="What is the purpose of data cleaning?", activity=a17
    )
    q15 = Question(
        id=uuid.uuid4(),
        statement="Who is responsible for managing and prioritizing the product backlog in Scrum?",
        activity=a20,
    )
    q16 = Question(
        id=uuid.uuid4(),
        statement="What is the purpose of the Daily Scrum?",
        activity=a20,
    )
    q17 = Question(
        id=uuid.uuid4(),
        statement="Under GDPR, what is the maximum time to notify a data breach to the supervisory authority?",
        activity=a22,
    )
    q18 = Question(
        id=uuid.uuid4(),
        statement="Which GDPR principle requires collecting only the minimum data necessary for the stated purpose?",
        activity=a22,
    )
    q19 = Question(
        id=uuid.uuid4(),
        statement="What is the primary purpose of a call to action (CTA) in copywriting?",
        activity=a24,
    )
    q20 = Question(
        id=uuid.uuid4(),
        statement="Which headline technique typically increases click-through rates?",
        activity=a24,
    )
    q21 = Question(id=uuid.uuid4(), statement="What is a content pillar?", activity=a27)
    q22 = Question(
        id=uuid.uuid4(),
        statement="Why is audience persona definition important in content strategy?",
        activity=a27,
    )
    q23 = Question(
        id=uuid.uuid4(),
        statement="Which metric measures the percentage of users who clicked a link after seeing a post?",
        activity=a29,
    )
    q24 = Question(
        id=uuid.uuid4(),
        statement="What does 'engagement rate' measure on social media?",
        activity=a29,
    )
    q25 = Question(
        id=uuid.uuid4(),
        statement="What is the recommended first step when a client raises a complaint?",
        activity=a31,
    )
    q26 = Question(
        id=uuid.uuid4(),
        statement="What does active listening involve in a support context?",
        activity=a31,
    )
    session.add_all(
        [
            q1,
            q2,
            q3,
            q4,
            q5,
            q6,
            q7,
            q8,
            q9,
            q10,
            q11,
            q12,
            q13,
            q14,
            q15,
            q16,
            q17,
            q18,
            q19,
            q20,
            q21,
            q22,
            q23,
            q24,
            q25,
            q26,
        ]
    )
    session.commit()

    # --- Answers ---
    session.add_all(
        [
            Answer(id=uuid.uuid4(), content="git start", is_correct=False, question=q1),
            Answer(id=uuid.uuid4(), content="git init", is_correct=True, question=q1),
            Answer(
                id=uuid.uuid4(), content="git create", is_correct=False, question=q1
            ),
            Answer(id=uuid.uuid4(), content="git new", is_correct=False, question=q1),
            Answer(
                id=uuid.uuid4(), content="git commit -a", is_correct=False, question=q2
            ),
            Answer(id=uuid.uuid4(), content="git push", is_correct=False, question=q2),
            Answer(id=uuid.uuid4(), content="git add .", is_correct=True, question=q2),
            Answer(id=uuid.uuid4(), content="git stage", is_correct=False, question=q2),
            Answer(id=uuid.uuid4(), content="tuple", is_correct=False, question=q3),
            Answer(id=uuid.uuid4(), content="str", is_correct=False, question=q3),
            Answer(id=uuid.uuid4(), content="list", is_correct=True, question=q3),
            Answer(id=uuid.uuid4(), content="int", is_correct=False, question=q3),
            Answer(
                id=uuid.uuid4(),
                content="A class variable shared across instances",
                is_correct=False,
                question=q4,
            ),
            Answer(
                id=uuid.uuid4(),
                content="The constructor, called when creating an instance",
                is_correct=True,
                question=q4,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A static method",
                is_correct=False,
                question=q4,
            ),
            Answer(
                id=uuid.uuid4(), content="A destructor", is_correct=False, question=q4
            ),
            Answer(id=uuid.uuid4(), content="WHERE", is_correct=False, question=q5),
            Answer(id=uuid.uuid4(), content="HAVING", is_correct=True, question=q5),
            Answer(id=uuid.uuid4(), content="GROUP BY", is_correct=False, question=q5),
            Answer(id=uuid.uuid4(), content="ORDER BY", is_correct=False, question=q5),
            Answer(
                id=uuid.uuid4(), content="INNER JOIN", is_correct=False, question=q6
            ),
            Answer(id=uuid.uuid4(), content="LEFT JOIN", is_correct=False, question=q6),
            Answer(
                id=uuid.uuid4(), content="FULL OUTER JOIN", is_correct=True, question=q6
            ),
            Answer(
                id=uuid.uuid4(), content="CROSS JOIN", is_correct=False, question=q6
            ),
            Answer(
                id=uuid.uuid4(),
                content="A running instance of a container",
                is_correct=False,
                question=q7,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A read-only template used to create containers",
                is_correct=True,
                question=q7,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A network configuration file",
                is_correct=False,
                question=q7,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A volume mounted to a container",
                is_correct=False,
                question=q7,
            ),
            Answer(
                id=uuid.uuid4(),
                content="docker-compose.yml",
                is_correct=False,
                question=q8,
            ),
            Answer(
                id=uuid.uuid4(), content=".dockerignore", is_correct=False, question=q8
            ),
            Answer(id=uuid.uuid4(), content="Dockerfile", is_correct=True, question=q8),
            Answer(id=uuid.uuid4(), content="Makefile", is_correct=False, question=q8),
            Answer(id=uuid.uuid4(), content="POST", is_correct=False, question=q9),
            Answer(id=uuid.uuid4(), content="PUT", is_correct=False, question=q9),
            Answer(id=uuid.uuid4(), content="PATCH", is_correct=True, question=q9),
            Answer(id=uuid.uuid4(), content="GET", is_correct=False, question=q9),
            Answer(id=uuid.uuid4(), content="200 OK", is_correct=False, question=q10),
            Answer(
                id=uuid.uuid4(), content="201 Created", is_correct=True, question=q10
            ),
            Answer(
                id=uuid.uuid4(),
                content="204 No Content",
                is_correct=False,
                question=q10,
            ),
            Answer(
                id=uuid.uuid4(),
                content="400 Bad Request",
                is_correct=False,
                question=q10,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Continuous Infrastructure",
                is_correct=False,
                question=q11,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Controlled Integration",
                is_correct=False,
                question=q11,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Continuous Integration",
                is_correct=True,
                question=q11,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Code Inspection",
                is_correct=False,
                question=q11,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A scheduled daily cron job",
                is_correct=False,
                question=q12,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A push or pull request to the repository",
                is_correct=True,
                question=q12,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A database backup",
                is_correct=False,
                question=q12,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A server restart",
                is_correct=False,
                question=q12,
            ),
            Answer(
                id=uuid.uuid4(), content="df.describe()", is_correct=False, question=q13
            ),
            Answer(
                id=uuid.uuid4(), content="df.head()", is_correct=False, question=q13
            ),
            Answer(id=uuid.uuid4(), content="df.info()", is_correct=True, question=q13),
            Answer(
                id=uuid.uuid4(), content="df.summary()", is_correct=False, question=q13
            ),
            Answer(
                id=uuid.uuid4(),
                content="Visualizing data in charts",
                is_correct=False,
                question=q14,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Removing or correcting inaccurate, incomplete or duplicate records",
                is_correct=True,
                question=q14,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Training a machine learning model",
                is_correct=False,
                question=q14,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Writing SQL queries",
                is_correct=False,
                question=q14,
            ),
            Answer(
                id=uuid.uuid4(), content="Scrum Master", is_correct=False, question=q15
            ),
            Answer(
                id=uuid.uuid4(),
                content="Development Team",
                is_correct=False,
                question=q15,
            ),
            Answer(
                id=uuid.uuid4(), content="Product Owner", is_correct=True, question=q15
            ),
            Answer(
                id=uuid.uuid4(), content="Stakeholder", is_correct=False, question=q15
            ),
            Answer(
                id=uuid.uuid4(),
                content="To review the sprint backlog with stakeholders",
                is_correct=False,
                question=q16,
            ),
            Answer(
                id=uuid.uuid4(),
                content="To plan the next sprint",
                is_correct=False,
                question=q16,
            ),
            Answer(
                id=uuid.uuid4(),
                content="To synchronize the team and identify blockers",
                is_correct=True,
                question=q16,
            ),
            Answer(
                id=uuid.uuid4(),
                content="To demonstrate completed work",
                is_correct=False,
                question=q16,
            ),
            Answer(id=uuid.uuid4(), content="24 hours", is_correct=False, question=q17),
            Answer(id=uuid.uuid4(), content="48 hours", is_correct=False, question=q17),
            Answer(id=uuid.uuid4(), content="72 hours", is_correct=True, question=q17),
            Answer(id=uuid.uuid4(), content="7 days", is_correct=False, question=q17),
            Answer(id=uuid.uuid4(), content="Accuracy", is_correct=False, question=q18),
            Answer(
                id=uuid.uuid4(),
                content="Storage limitation",
                is_correct=False,
                question=q18,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Data minimisation",
                is_correct=True,
                question=q18,
            ),
            Answer(
                id=uuid.uuid4(), content="Integrity", is_correct=False, question=q18
            ),
            Answer(
                id=uuid.uuid4(),
                content="To describe the product in detail",
                is_correct=False,
                question=q19,
            ),
            Answer(
                id=uuid.uuid4(),
                content="To prompt the reader to take a specific next step",
                is_correct=True,
                question=q19,
            ),
            Answer(
                id=uuid.uuid4(),
                content="To list company achievements",
                is_correct=False,
                question=q19,
            ),
            Answer(
                id=uuid.uuid4(),
                content="To improve SEO ranking",
                is_correct=False,
                question=q19,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Using long, technical descriptions",
                is_correct=False,
                question=q20,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Being vague to create curiosity",
                is_correct=False,
                question=q20,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Including a specific number or benefit",
                is_correct=True,
                question=q20,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Avoiding action verbs",
                is_correct=False,
                question=q20,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A type of social media post format",
                is_correct=False,
                question=q21,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A core topic or theme around which content is created consistently",
                is_correct=True,
                question=q21,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A technical SEO element",
                is_correct=False,
                question=q21,
            ),
            Answer(
                id=uuid.uuid4(),
                content="A project management tool",
                is_correct=False,
                question=q21,
            ),
            Answer(
                id=uuid.uuid4(),
                content="It determines the color scheme of marketing materials",
                is_correct=False,
                question=q22,
            ),
            Answer(
                id=uuid.uuid4(),
                content="It ensures content addresses the specific needs and context of target readers",
                is_correct=True,
                question=q22,
            ),
            Answer(
                id=uuid.uuid4(),
                content="It replaces the need for an editorial calendar",
                is_correct=False,
                question=q22,
            ),
            Answer(
                id=uuid.uuid4(),
                content="It automatically generates content ideas",
                is_correct=False,
                question=q22,
            ),
            Answer(
                id=uuid.uuid4(), content="Impressions", is_correct=False, question=q23
            ),
            Answer(id=uuid.uuid4(), content="Reach", is_correct=False, question=q23),
            Answer(
                id=uuid.uuid4(),
                content="Click-through rate (CTR)",
                is_correct=True,
                question=q23,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Follower growth rate",
                is_correct=False,
                question=q23,
            ),
            Answer(
                id=uuid.uuid4(),
                content="The total number of followers gained in a period",
                is_correct=False,
                question=q24,
            ),
            Answer(
                id=uuid.uuid4(),
                content="The ratio of interactions (likes, comments, shares) to total reach or impressions",
                is_correct=True,
                question=q24,
            ),
            Answer(
                id=uuid.uuid4(),
                content="The frequency of posts published per week",
                is_correct=False,
                question=q24,
            ),
            Answer(
                id=uuid.uuid4(),
                content="The number of ad impressions served",
                is_correct=False,
                question=q24,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Offer an immediate refund",
                is_correct=False,
                question=q25,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Transfer the call to a manager",
                is_correct=False,
                question=q25,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Acknowledge the issue and show empathy",
                is_correct=True,
                question=q25,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Explain why the issue is not your fault",
                is_correct=False,
                question=q25,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Responding quickly without letting the client finish",
                is_correct=False,
                question=q26,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Taking notes and summarizing the client's concern back to them",
                is_correct=True,
                question=q26,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Avoiding eye contact to stay neutral",
                is_correct=False,
                question=q26,
            ),
            Answer(
                id=uuid.uuid4(),
                content="Multitasking to handle multiple clients at once",
                is_correct=False,
                question=q26,
            ),
        ]
    )
    session.commit()

    # --- Role skills ---
    r1.skills.extend([sk1, sk2, sk3, sk4, sk7])
    r2.skills.extend([sk1, sk4, sk7, sk12])
    r3.skills.extend([sk9, sk10, sk11])
    r4.skills.extend([sk4, sk5, sk6, sk8])
    r5.skills.extend([sk9, sk10, sk19])
    r6.skills.extend([sk13, sk14, sk22])
    r7.skills.extend([sk13, sk14, sk15, sk17])
    r8.skills.extend([sk16, sk17, sk22])
    r9.skills.extend([sk19, sk20, sk22])
    r10.skills.extend([sk1, sk3, sk18])
    r11.skills.extend([sk16, sk21])
    session.commit()

    # --- Employee skills ---
    e1.skills.extend([sk1, sk3, sk4])
    e2.skills.extend([sk1, sk2, sk4])
    e3.skills.extend([sk1, sk4, sk7])
    e4.skills.extend([sk1, sk3, sk7])
    e5.skills.extend([sk1, sk4, sk12])
    e6.skills.extend([sk1, sk4, sk7, sk12])
    e7.skills.extend([sk4, sk5, sk6, sk8])
    e8.skills.extend([sk4, sk5, sk8])
    e9.skills.extend([sk9, sk10, sk11])
    e10.skills.extend([sk9, sk10, sk19])
    e11.skills.extend([sk3, sk18, sk22])
    e12.skills.extend([sk13, sk14, sk22])
    e13.skills.extend([sk13, sk14, sk15, sk17])
    e14.skills.extend([sk16, sk17, sk22])
    e15.skills.extend([sk16, sk21])
    e16.skills.extend([sk19, sk20, sk22])
    session.commit()

    # --- Course skills ---
    c1.skills.extend([sk4])
    c2.skills.extend([sk1])
    c3.skills.extend([sk3])
    c4.skills.extend([sk5])
    c5.skills.extend([sk1, sk7])
    c6.skills.extend([sk4, sk6])
    c7.skills.extend([sk1, sk3, sk18])
    c8.skills.extend([sk9])
    c10.skills.extend([sk17])
    c11.skills.extend([sk14, sk17])
    c12.skills.extend([sk13, sk14, sk15])
    c13.skills.extend([sk21])
    session.commit()

    # --- Enrollments ---
    session.add_all([
        Enrollment(id=uuid.uuid4(), employee=e1, course=c2, status=EnrollmentStatus.COMPLETED),
        Enrollment(id=uuid.uuid4(), employee=e1, course=c3, status=EnrollmentStatus.ENROLLED),
        Enrollment(id=uuid.uuid4(), employee=e5, course=c1, status=EnrollmentStatus.COMPLETED),
        Enrollment(id=uuid.uuid4(), employee=e5, course=c6, status=EnrollmentStatus.CERTIFIED, certification_date=datetime(2025, 3, 15)),
        Enrollment(id=uuid.uuid4(), employee=e6, course=c8, status=EnrollmentStatus.CERTIFIED, certification_date=datetime(2024, 11, 20)),
        Enrollment(id=uuid.uuid4(), employee=e6, course=c5, status=EnrollmentStatus.IN_PROGRESS),
        Enrollment(id=uuid.uuid4(), employee=e7, course=c4, status=EnrollmentStatus.COMPLETED),
        Enrollment(id=uuid.uuid4(), employee=e7, course=c6, status=EnrollmentStatus.CERTIFIED, certification_date=datetime(2024, 6, 1)),
        Enrollment(id=uuid.uuid4(), employee=e9, course=c8, status=EnrollmentStatus.EXPIRED, certification_date=datetime(2023, 5, 10)),
        Enrollment(id=uuid.uuid4(), employee=e11, course=c3, status=EnrollmentStatus.COMPLETED),
        Enrollment(id=uuid.uuid4(), employee=e11, course=c7, status=EnrollmentStatus.IN_PROGRESS),
        Enrollment(id=uuid.uuid4(), employee=e13, course=c10, status=EnrollmentStatus.COMPLETED),
        Enrollment(id=uuid.uuid4(), employee=e13, course=c12, status=EnrollmentStatus.CERTIFIED, certification_date=datetime(2025, 1, 8)),
        Enrollment(id=uuid.uuid4(), employee=e15, course=c13, status=EnrollmentStatus.COMPLETED),
        Enrollment(id=uuid.uuid4(), employee=e15, course=c9, status=EnrollmentStatus.ENROLLED),
        Enrollment(id=uuid.uuid4(), employee=e16, course=c9, status=EnrollmentStatus.CERTIFIED, certification_date=datetime(2025, 2, 28)),
        Enrollment(id=uuid.uuid4(), employee=e16, course=c8, status=EnrollmentStatus.ENROLLED),
    ])
    session.commit()
