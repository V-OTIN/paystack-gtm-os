# Loom script: Week 2 Clay table (W1 FCCPC approved lenders)

About 5 minutes, one take. Words in **[brackets]** are what to show on screen. Read the rest out loud.

---

## 1. Intro (30 seconds)

**[Clay workbook open on the Lenders table]**

Hi, I'm Valentine. This is my Week 2 Clay table for Paystack. The workflow is called FCCPC approved lenders.

The idea is simple. In Nigeria, every digital lender has to be approved by the FCCPC, the consumer protection regulator. A lender that has just been approved now needs to collect repayments and pay out loans. That is the moment Paystack is useful. So the regulator's register is my list, and the approval is my signal.

## 2. The three tables (30 seconds)

**[Click through the three tabs at the bottom]**

The workbook has three tables.

Exclusions holds the companies I must never email: Paystack's competitors, named Paystack customers, and companies Paystack owns.

Lenders is the FCCPC register, imported as a CSV. 526 lenders.

Contacts holds the people at those lenders.

The table is on manual, so nothing paid runs unless I choose to run it.

## 3. The list and the free checks (45 seconds)

**[Lenders table: show Company Name Clean, App Count, Domain From App, In Batch?]**

I didn't use a Clay search for the list. The FCCPC register is the source of truth, so I imported it as a CSV. A search would give me companies that look like lenders. The register gives me companies the regulator actually approved.

These first columns are all formulas, so they're free. They clean the company name, count the lender's apps, and pull a website from the app details where one is listed.

I kept the batch small on purpose. In Batch? limits paid work to the first 45 rows, so I could prove each step before spending more.

## 4. Website, AI column and company gates (60 seconds)

**[Show the Lender Website Claygent column, open one cell to show evidence and confidence]**

This is my AI column. A Claygent finds each lender's real website and returns a confidence score with evidence. It only scores "high" if it actually opened a page on that domain. That rule came from a mistake: in my first test it marked a domain "high" from a LinkedIn mention, and the domain didn't even load. So I tightened the prompt.

**[Show Company Domain Override and Company Domain]**

Where the AI was wrong, for example parked or for-sale domains, I added a manual override. A dash drops the row.

**[Show the Exclusions lookup and Pass Company Gates?]**

Then a lookup checks each domain against Exclusions. It caught Branch, a named Paystack customer, and Allawee, which Paystack owns. Lookups are free.

## 5. Signal and routing (45 seconds)

**[Show Tech Stack, Gateway Status, Company Ready?, Cell]**

Tech Stack uses BuiltWith to see which payment gateway is on each lender's website. If Paystack is already there, the lender drops, because they're already a customer. That removed Nextpayday and Creditville.

If a competitor like Flutterwave is there, the lender goes to cell C, the switch angle. If nothing is found, it goes to cell D, the first-gateway angle.

Out of 45 lenders, 22 are Company Ready: 3 in cell C and 19 in cell D.

## 6. People and the contact gate (45 seconds)

**[Contacts table: show Persona, Title Rank, Chosen?, Ready to Contact?]**

In Contacts, Find People searches each ready lender's domain for two personas: a technical champion, like a CTO or head of engineering, and an economic buyer, like the CEO, CFO or founder.

Persona and Title Rank are formulas. Back in Lenders, Champion Pick and Buyer Pick choose the most senior person per persona, so I contact at most two people per lender.

Ready to Contact? is the gate. Only true rows get an email lookup. 21 people found, 12 passed.

## 7. Emails and the final gate (30 seconds)

**[Show Work Email waterfall, Email Domain OK?, Send Ready?]**

The work email waterfall runs only on those 12 rows. It found 10 emails.

Email Domain OK? checks that the email domain matches the lender's verified domain. Two didn't match, so they're held for review, not sent.

That leaves 8 Send Ready contacts.

## 8. Views, cost and close (30 seconds)

**[Click the Ready to send, Held and Dropped views]**

There are three views: Ready to send, Held, and Dropped, so anyone can see where each row ended up and why.

The whole build cost 52.1 credits. That's the AI column, BuiltWith, company enrichment and the email waterfall. Formulas, lookups and searches are free.

Funnel: 526 lenders, 45 in the batch, 22 ready, 21 people, 12 ready to contact, 10 emails, 8 ready to send.

Next week this moves into HubSpot. Thanks for watching.
