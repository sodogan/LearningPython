from string import Template


def main():
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    course_name = "Advanced Python"
    course_author = "Joe Marini"

    templ = Template("You're watching ${title} by ${author}")

    str2 = templ.substitute(title=course_name, author=course_author)
    print(str2)

    # Substitute dictionary
    data = {
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    print(templ.substitute(data))

    print(f"You're watching {course_name} by {course_author}")


if __name__ == "__main__":
    main()
