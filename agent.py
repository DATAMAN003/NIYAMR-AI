import json
import os
from PyPDF2 import PdfReader
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class UniversalCreditActAgent:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        self.extracted_text = ""
        
    def task1_extract_text(self):
        """Extract text from PDF"""
        print("Task 1: Extracting text from PDF...")
        reader = PdfReader(self.pdf_path)
        text_parts = []
        
        for page in reader.pages:
            text_parts.append(page.extract_text())
        
        self.extracted_text = "\n".join(text_parts)
        
        with open('extracted_text.txt', 'w', encoding='utf-8') as f:
            f.write(self.extracted_text)
        
        print(f"✓ Extracted {len(self.extracted_text)} characters from {len(reader.pages)} pages")
        return self.extracted_text
    
    def task2_summarize(self):
        """Summarize the Act in 5-10 bullet points"""
        print("\nTask 2: Summarizing the Act...")
        
        prompt = f"""Analyze this Universal Credit Act 2025 and provide a summary in 5-10 bullet points.
Focus on:
- Purpose
- Key definitions
- Eligibility
- Obligations
- Enforcement elements

Act text:
{self.extracted_text[:15000]}

Return ONLY a JSON array of bullet points like:
["point 1", "point 2", ...]"""
        
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        # Extract JSON if wrapped in markdown
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        data = json.loads(content)
        summary = data.get('summary', data) if isinstance(data, dict) else data
        print(f"✓ Generated {len(summary)} summary points")
        return summary
    
    def task3_extract_sections(self):
        """Extract key legislative sections"""
        print("\nTask 3: Extracting key legislative sections...")
        
        prompt = f"""Analyze this Universal Credit Act 2025 and extract the following sections.
Return a JSON object with these exact keys:

{{
  "definitions": "extracted definitions text",
  "obligations": "extracted obligations text",
  "responsibilities": "extracted responsibilities text",
  "eligibility": "extracted eligibility criteria text",
  "payments": "extracted payment/entitlement details",
  "penalties": "extracted penalties/enforcement text",
  "record_keeping": "extracted record-keeping/reporting requirements"
}}

Act text:
{self.extracted_text[:15000]}

Return ONLY valid JSON."""
        
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        # Extract JSON if wrapped in markdown
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        sections = json.loads(content)
        print("✓ Extracted all key sections")
        return sections
    
    def task4_rule_checks(self, sections):
        """Apply 6 rule checks"""
        print("\nTask 4: Applying rule checks...")
        
        rules = [
            "Act must define key terms",
            "Act must specify eligibility criteria",
            "Act must specify responsibilities of the administering authority",
            "Act must include enforcement or penalties",
            "Act must include payment calculation or entitlement structure",
            "Act must include record-keeping or reporting requirements"
        ]
        
        section_map = {
            rules[0]: sections.get('definitions', ''),
            rules[1]: sections.get('eligibility', ''),
            rules[2]: sections.get('responsibilities', ''),
            rules[3]: sections.get('penalties', ''),
            rules[4]: sections.get('payments', ''),
            rules[5]: sections.get('record_keeping', '')
        }
        
        results = []
        
        for rule in rules:
            content = section_map[rule]
            
            prompt = f"""Evaluate if this rule is satisfied: "{rule}"

Content: {content[:1000]}

Return JSON:
{{
  "rule": "{rule}",
  "status": "pass" or "fail",
  "evidence": "specific section or quote",
  "confidence": 0-100
}}"""
            
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            # Extract JSON if wrapped in markdown
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
            result = json.loads(content)
            results.append(result)
            print(f"  ✓ {result['rule']}: {result['status']} ({result['confidence']}%)")
        
        return results
    
    def generate_report(self):
        """Generate complete JSON report"""
        print("\n" + "="*60)
        print("UNIVERSAL CREDIT ACT 2025 - AI AGENT ANALYSIS")
        print("="*60)
        
        # Task 1
        text = self.task1_extract_text()
        
        # Task 2
        summary = self.task2_summarize()
        
        # Task 3
        sections = self.task3_extract_sections()
        
        # Task 4
        rule_checks = self.task4_rule_checks(sections)
        
        # Compile final report
        report = {
            "document": "Universal Credit Act 2025",
            "analysis_date": "2025-11-20",
            "ai_model": "Groq - Llama 3.3 70B Versatile",
            
            "task_1_extract_text": {
                "task_name": "Extract Text from PDF",
                "status": "complete",
                "characters_extracted": len(text),
                "pages_processed": 21,
                "output_file": "extracted_text.txt",
                "method": "PyPDF2"
            },
            
            "task_2_summarize_act": {
                "task_name": "Summarize the Act in 5-10 Bullet Points",
                "summary_points": summary,
                "total_points": len(summary)
            },
            
            "task_3_extract_sections": {
                "task_name": "Extract Key Legislative Sections",
                "sections": sections
            },
            
            "task_4_rule_checks": {
                "task_name": "Apply 6 Rule Compliance Checks",
                "rules_checked": 6,
                "rules_passed": sum(1 for r in rule_checks if r['status'] == 'pass'),
                "rules_failed": sum(1 for r in rule_checks if r['status'] == 'fail'),
                "checks": rule_checks
            }
        }
        
        # Save report
        with open('output_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print("\n" + "="*60)
        print("✓ ANALYSIS COMPLETE")
        print("="*60)
        print(f"Report saved to: output_report.json")
        print(f"Extracted text saved to: extracted_text.txt")
        
        return report


def main():
    agent = UniversalCreditActAgent('ukpga_20250022_en.pdf')
    report = agent.generate_report()
    
    print("\n📊 Task 2 - Summary:")
    for i, point in enumerate(report['task_2_summarize_act']['summary_points'], 1):
        print(f"  {i}. {point}")
    
    print("\n✅ Task 4 - Rule Check Results:")
    for check in report['task_4_rule_checks']['checks']:
        status_icon = "✓" if check['status'] == 'pass' else "✗"
        print(f"  {status_icon} {check['rule']} - {check['confidence']}%")
    
    print(f"\n📈 Overall: {report['task_4_rule_checks']['rules_passed']}/6 rules passed")


if __name__ == "__main__":
    main()
