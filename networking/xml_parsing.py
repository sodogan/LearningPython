import xml.dom.minidom as xml_dom


def main():
    doc = xml_dom.parse("samplexml.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")
    print("{} skills:".format(skills.length))
    for skill in skills:
        print(f' - {skill.getAttribute("name")}')

    new_skill = doc.createElement("skill")
    new_skill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(new_skill)

    skills = doc.getElementsByTagName("skill")
    print("Updated {} skills:".format(skills.length))
    for skill in skills:
        print(f' - {skill.getAttribute("name")}')


if __name__ == "__main__":
    main()
