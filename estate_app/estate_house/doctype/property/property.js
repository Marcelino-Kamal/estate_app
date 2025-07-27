// Copyright (c) 2025, Marco and contributors
// For license information, please see license.txt

frappe.ui.form.on("Property", {
    setup: frm=>{
       frm.check_duplication = function(frm , new_value){
            console.log(new_value.amenity + " " + new_value.name );
            frm.doc.amenities.forEach(element => {
               if(new_value.amenity == element.amenity && element.name != new_value.name ){
                    new_value.amenity = ''
                    frappe.throw(msg=`there is a duplicated amenity`)
                    frm.refresh_field('amenities');
               }
            });
        }
        frm.check_comptability =  function (frm,new_value){
            console.log(frm.doc.type)
            if(new_value.amenity == "Outdoor Kitchens" && frm.doc.type == "Flat"){
                new_value.amenity = ''
                frappe.throw(msg=`The Outdoors Kitchens can't exists in ${frm.doc.type}`)
                frm.refresh_field('amenities')
            }
        }
        frm.compute_total = function(frm){
            let total_amenities = 0;
            //llop through amenitites
            frm.doc.amenities.forEach(x =>{
                total_amenities += x.amenity_price;
            })
            let grand = frm.doc.property_price + total_amenities;
            if(frm.doc.discount > 0){
                grand -= (grand * (frm.doc.discount/100))
            }
            console.log (grand)

            frm.set_value('grant_total',grand)
        }
    
    },
    //setup: function(frm){
    // 
    //  console.log(frm)
    // },
	refresh(frm) {
        frm.add_custom_button('Button Name',()=>{
            console.log('Help me')
        },"Action");
        frm.add_custom_button('Say Hi',()=>{
            frappe.msgprint(msg="Hello ppl",title="Say Hi")
        },"Action");
        frm.add_custom_button('Say Bye',()=>{
            console.log('Bye Bye')
        },"Action");
        frm.add_custom_button('Prompt Change address',()=>{
            frappe.prompt('Address',({value})=>{
                if(value){
                    frm.set_value('address',value);
                    frm.refresh_field('address'); // refresh field in the form
                    frappe.msgprint(msg="Address been updated");
                }
            })
        });
        //Check property types
        frm.add_custom_button('Same type',()=>{
            let Ptype = frm.doc.type;
            console.log(Ptype)
            // call api
            frappe.call({
				method: "estate_app.estate_house.doctype.property.api.getPropertyType", 
                args:{'type': Ptype},
				callback: function (r) {
                    console.log(r)
                    if(r.message.length>0){
                        let header = `<h3> Properties if same type: ${Ptype}</h3>`;
                        let body = ``;
                        r.message.forEach(x =>{
                            let cont = `<p>Name: ${x.name}: <a href='/app/property/${x.name}'>Visit</a></p>`
                            body  = body + cont;
                        })
                        let all = header + body;
                        frappe.msgprint(msg=`${all}`)
                    }
					
				},
			});   
            
        });
        
	},
    property_price: function(frm){
        frm.compute_total(frm);
    },
    discount : function(frm){
        frm.compute_total(frm);
    },
    // onload(frm){
    //     frm.compute_total(frm)
    // }
   
});

//Amentites Child table
                //refer-to the DocType
frappe.ui.form.on('Property Amenity Details',{
   
    amenity: function(frm,cdt,cdn){
        //to grab the entire record
         let row = locals[cdt][cdn];
        //console.log(row.amaneity);
        frm.check_comptability(frm,row)
        frm.check_duplication(frm,row)
    },
     //calculate total of amenity
     amenity_price(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frm.compute_total(frm);
    },
    amenities_remove: function(frm,cdt,cdn){
       frm.compute_total(frm)
    }



});



