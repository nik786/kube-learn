

রোহিত শর্মার Terraform রাজ্য (সকল চরিত্র সহ)

একদিন রোহিত শর্মা নিজের জন্য এক বিশাল রাজ্য বানালো।
রাজ্যের নাম দিল – aws_vpc (VPC কমপ্লেক্স)।

🏰 VPC কমপ্লেক্স

এই কমপ্লেক্সের চারপাশে বিশাল এক CIDR Block দেয়াল টানা হলো।
রাজ্যে সক্রিয় হলো –

DNS Support

DNS Hostnames

Instance Tenancy

🏘️ দুই পাড়া: Public ও Private

রোহিতের রাজ্যে দুইটা বড় পাড়া হলো –

aws_subnet Public Subnet

রাজ্যের পূর্ব দিকের খোলা পাড়া।

এখানে for_each loop দিয়ে অনেক ঘর বানানো যায়।

প্রতিটা ঘরের আলাদা vpc_id আর ছোট cidr_block থাকে।

যেহেতু এটি পাবলিক, তাই এখানে দরজা সবসময় খোলা থাকে (Internet Access)।

aws_subnet Private Subnet

এটি হলো অন্দরমহল – শান্ত আর সুরক্ষিত পাড়া।

এখানকার ঘরগুলো বাইরের লোকেরা দেখতে পায় না।

Private Subnet-এর দরজা সবসময় বন্ধ থাকে।

কিন্তু অন্দরমহলের মানুষও তো কখনও কখনও বাইরের জিনিসপত্র চায়!

তখন তারা একটা গোপন রাস্তা ব্যবহার করে – সেটাই হলো NAT Gateway।

🌉 NAT Gateway (গোপন সেতু)

অন্দরমহল থেকে সরাসরি বাইরের রাস্তা নেই।
তাই Public Subnet-এর ভেতরে একটা aws_nat_gateway বানানো হলো।
এটা হলো একধরনের গোপন সেতু, যেটা দিয়ে Private Subnet-এর মানুষরা বাইরে বার্তা পাঠাতে পারে,
কিন্তু বাইরের মানুষ সরাসরি অন্দরমহলে ঢুকতে পারে না।

NAT Gateway বসানো হলো Public Subnet-এর ভেতরে।

এর সাথে যুক্ত হলো একটা Elastic IP – যেন বাইরের দুনিয়ার সাথে যোগাযোগ করতে পারে।

🛣️ Public Route (রাজপথ)

Public Subnet-এর মানুষদের বাইরে যেতে হলে রাজপথ লাগে।
সেই রাজপথ Terraform এ হলো – aws_route Public Route।

এই রাস্তা বানাতে লাগে –

unique vpc_id

cidr_block (0.0.0.0/0) – সবার জন্য খোলা রাস্তা

gateway_id – যেটা aws_internet_gateway-এর সাথে যুক্ত থাকে।

📜 Route Tables (মানচিত্র)

Public Route Table

Public Subnet-এর ঘরগুলো এই মানচিত্র ব্যবহার করে।

এখানে 0.0.0.0/0 রাস্তাটা সরাসরি Internet Gateway-তে নিয়ে যায়।

Private Route Table

Private Subnet-এর ঘরগুলো এই মানচিত্র ব্যবহার করে।

এখানে 0.0.0.0/0 রাস্তাটা সরাসরি NAT Gateway-তে নিয়ে যায়।

ফলে অন্দরমহল থেকে বাইরের দুনিয়ায় বার্তা যায়,
কিন্তু বাইরের কেউ সরাসরি অন্দরমহলে ঢুকতে পারে না।

🌐 Internet Gateway (বিশ্ব দরজা)

রাজ্যের বিশাল দরজার নাম হলো – aws_internet_gateway।
এটাই Public Subnet-এর লোকদের বাইরের দুনিয়ার সাথে কথা বলার একমাত্র পথ।
এর গায়ে অবশ্যই লেখা থাকে কোন vpc_id-র জন্য এটি খোলা।

🎉 সারাংশ (চরিত্র তালিকা)

রাজা → aws_vpc

খোলা পাড়া → aws_subnet Public Subnet

অন্দরমহল → aws_subnet Private Subnet

বিশ্ব দরজা → aws_internet_gateway

রাজপথ → aws_route

মানচিত্র → aws_route_table

পাড়া-মানচিত্র যোগসূত্র → aws_route_table_association

গোপন সেতু → aws_nat_gateway

চিহ্ন (পাসপোর্ট) → Elastic IP (aws_eip)
