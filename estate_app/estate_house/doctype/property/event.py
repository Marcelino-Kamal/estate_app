import frappe
from estate_app.utils import sendmail 


def validate(doc, event):
    pass
    # print(f"{doc}{event}")
    # frappe.throw("Error Occured")
def on_update(doc,event):
    frappe.msgprint(msg="Congratz you have updated the record",title="Update",indicator='blue')
def afterInsert(doc,event):
    #create note on property insert!!
    note = frappe.get_doc({
        'doctype':'Note',
        'title':f"Property :{doc.name}",
        'public':True,
        'content':doc.description
    })
    note.insert()
    frappe.db.commit()
    frappe.msgprint(f"{note.title} has been created")
    #send mail
    agent_email = frappe.get_doc('Agent',doc.agent_email)
    sendmail(doc,[agent_email,'_test@test.com'],
             f"Hello <b>{doc.agent_name}, a property has been created on you behalf</b>",'New Property',
             [frappe.attach_print(doc.doctype,doc.name,file_name=doc.name)])
