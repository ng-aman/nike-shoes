class item:
    def __init__(self,itm_name, itm_price):
        self.itm_name = itm_name
        self.itm_price = itm_price


class ORDER:
    def __init__(self):
        self.its = []

    def AddItem(self, itm_name, quantity):
        self.its.append({"itm_name": itm_name, "quantity":quantity})

    def total(self):
        ttl= 0
        for item in self.its:
            ttl += item["itm_name"].itm_price* item["quantity"]
        return ttl


class billgenerator:
    def __init__(self, order):
        self.order = order

    def generate_bill(self):
        total_amt = self.order.ttl()
        service_tax = 0.05 * total_amt # Assuming 5% service tax
        gst = 0.18 * total_amt  # Assuming 18% GST

        final_amt =  total_amt +service_tax = 0.05 * total_amt + gst # Assuming 5% service tax
 

        # Display the bill
        print("------ Bill ------")
        for item in self.order.its:
            print(f"{item['itm_name'].itm_name} x {item['quantity']}: {item['itm_name'].itm_price * item['quantity']}")

        print(f"\nTotal Amount: {total_amt}")
        print(f"Service Tax (5%): {service_tax}")
        print(f"GST (18%): {gst}")
        print(f"Final Amount: {final_amt}")


# Example usage:
item1 = i("item1", 10.0)
item2 = i("item2", 15.0)

order = ORDER()
order.AddItem(item1, 2)
order.AddItem(item2, 1)

bill_generator = billgenerator(order)
bill_generator.generate_bill()
