from service import Service


class MenuUA(Service):
    async def run(self):
        await self.post(
            "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
            headers={"X-Requested-With": "XMLHttpRequest"},
            data={
                "user_info[fullname]": self.russian_name,
                "user_info[phone]": self.formatted_phone,
                "user_info[email]": self.email,
                "user_info[password]": self.password,
                "user_info[conf_password]": self.password,
            },
        )
        await self.post(
            "https://www.menu.ua/kiev/delivery/profile/show-verify.html",
            headers={"X-Requested-With": "XMLHttpRequest"},
            data={
                "phone": self.formatted_phone,
                "do": "phone"
            },
        )